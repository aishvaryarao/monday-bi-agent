# Monday.com Business Intelligence Agent

A conversational Business Intelligence (BI) agent that enables leadership teams to interact with business data stored in Monday.com using natural language.

The application retrieves live data from Monday.com through the GraphQL API, analyzes business metrics, and uses Google's Gemini model to generate concise, executive-friendly insights.

---

## Features

- Conversational chat interface
- Live Monday.com API integration
- Automatic data cleaning and preprocessing
- Business summary generation
- Executive-friendly insights powered by Gemini AI
- Streamlit web interface
- Cloud deployment using Streamlit Community Cloud

---

## Project Architecture

```
                +--------------------+
                |      User          |
                +---------+----------+
                          |
                          v
                +--------------------+
                |   Streamlit UI     |
                +---------+----------+
                          |
                          v
                +--------------------+
                | Monday API Client  |
                +---------+----------+
                          |
                          v
                +--------------------+
                |   Data Cleaner     |
                +---------+----------+
                          |
                          v
                +--------------------+
                | Business Analyzer  |
                +---------+----------+
                          |
                          v
                +--------------------+
                |   Gemini Client    |
                +---------+----------+
                          |
                          v
                +--------------------+
                | Business Insights  |
                +--------------------+
```

---

## Project Structure

```
monday-bi-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── services/
│   ├── analyzer.py
│   ├── gemini_client.py
│   └── monday_client.py
│
├── utils/
│   └── cleaner.py
│
├── prompts/
│   ├── system_prompt.txt
│   └── leadership_prompt.txt
│
└── docs/
    └── decision_log.md
```

---

## Tech Stack

- Python
- Streamlit
- Monday.com GraphQL API
- Google Gemini API
- Pandas
- HTTPX

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd monday-bi-agent
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in the project root.

```
MONDAY_API_TOKEN=your_token
GEMINI_API_KEY=your_api_key
DEALS_BOARD_ID=your_deals_board_id
WORK_ORDERS_BOARD_ID=your_work_orders_board_id
```

---

## Monday.com Configuration

1. Create or log in to your Monday.com account.
2. Create two boards:
   - Deals
   - Work Orders
3. Import the required datasets into the corresponding boards.
4. Generate a personal API token from **Admin → API**.
5. Copy the Board IDs for both boards.
6. Add the API token and board IDs to the `.env` file.

---

## Running the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Example Questions

- Give me a summary of the current business.
- Which deal stage has the highest number of deals?
- Show the distribution of work order statuses.
- Which sectors have the most work orders?
- Are there any business risks I should know about?

---

## Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Push the project to GitHub.
2. Connect the repository to Streamlit Community Cloud.
3. Add the required secrets:
   - MONDAY_API_TOKEN
   - GEMINI_API_KEY
   - DEALS_BOARD_ID
   - WORK_ORDERS_BOARD_ID
4. Deploy.

---

## Error Handling

The application handles:

- Invalid API credentials
- API request failures
- Missing or incomplete board data
- Empty responses from Monday.com
- Standardized column names during preprocessing

---

## Future Improvements

- Interactive dashboards
- Historical trend analysis
- Multi-workspace support
- PDF report export
- Authentication
- KPI visualizations
- Conversational memory