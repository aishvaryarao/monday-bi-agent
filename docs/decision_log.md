# Decision Log

## Project Overview

The objective of this project was to develop a conversational Business Intelligence (BI) agent that enables leadership teams to interact with business data stored in Monday.com using natural language. Instead of manually reviewing multiple boards and records, users can ask business-related questions and receive concise, executive-friendly insights.

The application retrieves live data from Monday.com through its GraphQL API, processes and summarizes the information using Python and Pandas, and uses Google's Gemini model to generate conversational responses. The solution is deployed on Streamlit Community Cloud, making it accessible through a web browser without requiring any local setup.

---

## Key Assumptions

The following assumptions were made during development:

- The Monday.com boards contain structured business data with a consistent schema.
- The imported Deals and Work Orders boards accurately represent current business information.
- Leadership users are interested in summarized business insights rather than raw records.
- The Gemini API is available for generating conversational responses.
- The volume of data is suitable for in-memory processing using Pandas.
- Users will interact with the system through natural language instead of writing database queries or filters.

---

## Design Decisions and Trade-offs

### 1. Streamlit for the User Interface

Streamlit was selected because it allows rapid development of interactive web applications using only Python. This reduced frontend complexity and allowed more time to focus on business logic, data processing, and API integration.

**Trade-off:** While Streamlit accelerates development, it provides less flexibility for highly customized user interfaces compared to frameworks such as React.

---

### 2. Monday.com GraphQL API for Data Retrieval

The application retrieves live data directly from Monday.com instead of relying on local CSV files. This ensures that responses are generated using the latest available information from the workspace.

**Trade-off:** The application depends on network connectivity and valid API credentials. If the API is unavailable, data cannot be retrieved.

---

### 3. Pandas for Data Processing

Pandas was used for cleaning, transforming, and analyzing board data because it offers efficient handling of structured datasets and simplifies aggregation operations.

**Trade-off:** Pandas works well for small to medium-sized datasets but may not be ideal for significantly larger datasets that require distributed processing.

---

### 4. Gemini for Conversational Responses

Instead of implementing rule-based responses, Google's Gemini model was used to understand user questions and generate natural, executive-friendly answers.

To reduce hallucinations, the model is provided with processed business summaries rather than unrestricted access to raw data.

**Trade-off:** Large language models can occasionally produce inaccurate interpretations. Providing structured summaries before prompting the model improves response reliability.

---

## Tech Stack Justification

| Technology | Reason for Selection |
|------------|----------------------|
| **Python** | Simple integration of APIs, data processing, and AI libraries within a single language. |
| **Streamlit** | Rapid development of an interactive conversational interface and straightforward deployment. |
| **Monday.com GraphQL API** | Provides live access to business data stored in Monday.com boards. |
| **Pandas** | Efficient data cleaning, transformation, and aggregation. |
| **Google Gemini** | Generates conversational responses and executive summaries from structured business insights. |
| **GitHub** | Version control and project management. |
| **Streamlit Community Cloud** | Simple cloud deployment with public accessibility for testing. |

---

## Leadership Updates Interpretation

The requirement for "leadership updates" was interpreted as generating concise executive summaries rather than displaying raw operational data.

The application focuses on presenting:

- Overall business performance
- Deal pipeline status
- Work order progress
- Distribution of business activities
- Potential risks and bottlenecks
- Actionable recommendations

This approach enables decision-makers to quickly understand the current business situation without reviewing individual records.

---

## Error Handling

The application includes basic error handling to improve reliability during execution.

- Invalid or missing API credentials are detected before data retrieval.
- API failures are handled without crashing the application.
- Missing or incomplete data is processed gracefully wherever possible.
- Data cleaning standardizes column names to avoid inconsistencies caused by imported datasets.

These measures improve the overall user experience while keeping the implementation lightweight.

---

## Future Improvements

With additional development time, the application could be extended by:

- Supporting multiple Monday.com workspaces and boards dynamically.
- Adding interactive dashboards and visualizations alongside conversational responses.
- Implementing response caching to reduce repeated API requests.
- Supporting historical trend analysis and KPI tracking.
- Exporting executive summaries as PDF or Excel reports.
- Adding authentication and role-based access control.
- Improving conversational memory for follow-up questions across a session.

---

## Conclusion

The primary objective of this project was to create a practical conversational BI assistant that combines live Monday.com data with natural language interaction. The final solution emphasizes simplicity, accessibility, and actionable business insights while remaining easy to deploy and maintain. The chosen architecture balances development speed, usability, and scalability, providing a strong foundation for future enhancements.