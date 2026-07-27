# Monday.com Business Intelligence Agent

A conversational Business Intelligence (BI) agent that enables leadership teams to interact with business data stored in Monday.com using natural language.

The application retrieves live data from Monday.com using the GraphQL API, processes and analyzes business metrics, and uses Google's Gemini model to generate concise, executive-friendly insights. It is deployed on Streamlit Community Cloud and can be accessed directly without any local setup.

---

## Live Demo

**Application:**  
https://monday-bi-agent-aish.streamlit.app/

---

## Features

- Conversational interface for business queries
- Live integration with Monday.com using the GraphQL API
- Automatic data cleaning and preprocessing
- Business metrics analysis and summarization
- Executive-friendly responses powered by Google Gemini
- Cloud deployment using Streamlit Community Cloud
- Graceful handling of API failures and data quality issues

---

## Architecture

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
├── .env.example
│
├── docs/
│   └── decision_log.md
│
├── prompts/
│   ├── system_prompt.txt
│   └── leadership_prompt.txt
│
├── services/
│   ├── analyzer.py
│   ├── gemini_client.py
│   └── monday_client.py
│
├── utils/
│   └── cleaner.py
```

---

## Tech Stack

- Python
- Streamlit
- Monday.com GraphQL API
- Google Gemini API
- Pandas
- HTTPX
- python-dotenv

---

## Setup

### Clone the repository

```bash
git clone https://github.com/aishvaryarao/monday-bi-agent.git
cd monday-bi-agent
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```env
MONDAY_API_TOKEN=your_monday_api_token
GEMINI_API_KEY=your_gemini_api_key
DEALS_BOARD_ID=your_deals_board_id
WORK_ORDERS_BOARD_ID=your_work_orders_board_id
```

---

## Monday.com Configuration

1. Create or sign in to your Monday.com account.
2. Create two boards:
   - Deals
   - Work Orders
3. Import the required datasets into the corresponding boards.
4. Generate a personal API token.
5. Obtain the Board IDs for both boards.
6. Add the API token and board IDs to the `.env` file.

---

## Running the Application

```bash
streamlit run app.py
```

---

## Example Questions

- Give me a summary of the current business.
- Which deal stage has the highest number of deals?
- Show the distribution of work order statuses.
- Which sectors have the most work orders?
- Are there any business risks that require attention?

---

## Deployment

The application is deployed using Streamlit Community Cloud.

Deployment steps:

1. Push the project to GitHub.
2. Connect the repository to Streamlit Community Cloud.
3. Configure the following secrets:
   - `MONDAY_API_TOKEN`
   - `GEMINI_API_KEY`
   - `DEALS_BOARD_ID`
   - `WORK_ORDERS_BOARD_ID`
4. Deploy the application.

---

## Error Handling

The application includes graceful error handling for:

- Missing environment variables
- Invalid API credentials
- Monday.com API failures
- Network and timeout errors
- Missing or incomplete board data
- Missing DataFrame columns
- Empty datasets
- Gemini API failures

---

## Future Improvements

- Interactive dashboards and visualizations
- Historical trend analysis
- Support for multiple Monday.com workspaces
- PDF and Excel report generation
- Authentication and role-based access
- Enhanced conversational memory

---

## Author

**Aishvarya V**
