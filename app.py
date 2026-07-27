from pathlib import Path
import os

import streamlit as st
from dotenv import load_dotenv

from services.monday_client import MondayClient
from services.analyzer import BusinessAnalyzer
from services.gemini_client import GeminiClient
from utils.cleaner import DataCleaner

load_dotenv()

st.set_page_config(
    page_title="Monday BI Agent",
    page_icon="♔",
    layout="wide"
)

st.title("♔ Monday.com Business Intelligence Agent")

# ----------------------------
# Validate Environment Variables
# ----------------------------
required_vars = [
    "MONDAY_API_TOKEN",
    "GEMINI_API_KEY",
    "DEALS_BOARD_ID",
    "WORK_ORDERS_BOARD_ID"
]

missing = [var for var in required_vars if not os.getenv(var)]

if missing:
    st.error(f"Missing environment variables: {', '.join(missing)}")
    st.stop()

# ----------------------------
# Load System Prompt
# ----------------------------
try:
    system_prompt = Path("prompts/system_prompt.txt").read_text(
        encoding="utf-8"
    )
except Exception as e:
    st.error(f"Unable to load system prompt: {e}")
    st.stop()

# ----------------------------
# Fetch Data from Monday.com
# ----------------------------
try:
    client = MondayClient()

    deals_items = client.get_board_items(
        os.getenv("DEALS_BOARD_ID")
    )

    work_orders_items = client.get_board_items(
        os.getenv("WORK_ORDERS_BOARD_ID")
    )

except Exception as e:
    st.error(f"Failed to retrieve data from Monday.com.\n\n{e}")
    st.stop()

# ----------------------------
# Clean Data
# ----------------------------
try:
    deals_df = DataCleaner.board_to_dataframe(deals_items)
    work_orders_df = DataCleaner.board_to_dataframe(work_orders_items)

    deals_df = DataCleaner.clean_dataframe(deals_df)
    work_orders_df = DataCleaner.clean_dataframe(work_orders_df)

except Exception as e:
    st.error(f"Error while processing data: {e}")
    st.stop()

# ----------------------------
# Check Empty Data
# ----------------------------
if deals_df.empty:
    st.warning("Deals board contains no data.")

if work_orders_df.empty:
    st.warning("Work Orders board contains no data.")

# ----------------------------
# Initialize Services
# ----------------------------
analyzer = BusinessAnalyzer(
    deals_df,
    work_orders_df
)

gemini = GeminiClient()

# ----------------------------
# Chat History
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Chat Input
# ----------------------------
if prompt := st.chat_input("Ask a business question..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        business_summary = analyzer.summary()

        final_prompt = f"""
{system_prompt}

Business Summary:
{business_summary}

User Question:
{prompt}

Answer as a business intelligence assistant.
"""

        response = gemini.generate_response(final_prompt)

    except Exception:
        response = (
            "Sorry, I couldn't process your request at the moment. "
            "Please try again later."
        )

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )