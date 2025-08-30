# 🧠 LLM SQL Assistant 🤖

This project is an LLM (Large Language Model) powered SQL assistant that allows users to interact with a SQLite database using natural language. It leverages the Gemini AI model to translate natural language questions into SQL queries, execute those queries against the database, and display the results in a user-friendly format. The assistant also provides explanations of the generated SQL queries, making it easier for users to understand the underlying logic. This tool simplifies database interaction, making it accessible to users without extensive SQL knowledge.

🚀 **Key Features**

*   **Natural Language to SQL Conversion:** Converts user's natural language questions into SQL queries using the Gemini AI model.
*   **SQL Query Execution:** Executes the generated SQL queries against a SQLite database.
*   **Result Display:** Presents the results of the SQL queries in a tabular format using Pandas.
*   **SQL Explanation:** Provides explanations of the generated SQL queries using the Gemini AI model.
*   **Interactive Streamlit UI:** Offers a user-friendly interface for interacting with the database.
*   **Query History:** Maintains a history of user questions and generated SQL queries.
*   **Database Schema Retrieval:** Retrieves and utilizes the database schema for accurate SQL generation.
*   **Error Handling:** Implements robust error handling for invalid SQL queries and other potential issues.

🛠️ **Tech Stack**

*   **Frontend:**
    *   Streamlit: For creating the interactive user interface.
*   **Backend:**
    *   Python: The primary programming language.
    *   google.generativeai: For interacting with the Gemini AI model.
*   **Database:**
    *   SQLite: For storing and managing the database.
*   **AI Tools:**
    *   Gemini AI: For natural language to SQL conversion and SQL explanation.
*   **Utilities:**
    *   pandas: For displaying query results in a tabular format.
    *   sqlite3: For interacting with the SQLite database.
    *   os: For accessing environment variables.
    *   datetime: For handling timestamps in the query history.
    *   dotenv: For loading environment variables from a `.env` file.
*   **Modules:**
    *   `modules/db_utils.py`: Custom module for database utilities.
    *   `modules/gemini_utils.py`: Custom module for Gemini AI interaction.

📦 **Getting Started**

### Prerequisites

*   Python 3.6 or higher
*   A Google Cloud project with the Gemini API enabled
*   A Gemini API key

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Create a `.env` file in the root directory and add your Gemini API key:

    ```
    GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
    ```

5.  Create the SQLite database and populate it with data:

    ```bash
    python sql.py
    ```

### Running Locally

1.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2.  Open your browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

📂 **Project Structure**

```
.
├── app.py                  # Main application file
├── sql.py                  # Script to create and populate the database
├── modules/                # Directory for custom modules
│   ├── db_utils.py         # Database utility functions
│   └── gemini_utils.py     # Gemini AI utility functions
├── .env                    # Environment variables (API key)
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```

📸 **Screenshots**

**1. Home Page – Connection Status**

When the app loads, it shows toast messages/notifications confirming successful connections to Gemini API and Database. If connections fail, error messages are displayed.

![alt text](https://github.com/AnandKumar56/Profile-asserts/blob/81e74189207322b236a25b19057f8d0b3ecd9d28/Screenshot%202025-08-31%20002649.png)

**2. Database Schema Viewer**

Displays the database schema with table details (Naresh_it_employee1) including column names and data types.

![alt text](https://github.com/AnandKumar56/Profile-asserts/blob/81e74189207322b236a25b19057f8d0b3ecd9d28/Screenshot%202025-08-31%20002718.png)

**3. Search History**

A detailed log of past queries with timeline, natural language input, generated SQL, and results. History is exportable as a CSV for review.

![alt text](https://github.com/AnandKumar56/Profile-asserts/blob/81e74189207322b236a25b19057f8d0b3ecd9d28/Screenshot%202025-08-31%20003510.png)

**4. About Page**

Provides a brief description of the project, its purpose, and key features like SQL generation, schema viewer, and history tracking.

![alt text](https://github.com/AnandKumar56/Profile-asserts/blob/81e74189207322b236a25b19057f8d0b3ecd9d28/Screenshot%202025-08-31%20003525.png)

**5. Query Execution – Full Page View**

Users enter natural language queries. The assistant generates the SQL query, executes it, displays results, and provides an explanation of the SQL logic — all in one view.

![alt text](https://github.com/AnandKumar56/Profile-asserts/blob/81e74189207322b236a25b19057f8d0b3ecd9d28/localhost_8501_.png)


🤝 **Contributing**

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.


📬 **Contact**

If you have any questions or suggestions, please feel free to contact me at [your_email@example.com](mailto:anandkumardalwaie1@gmail.com).

💖 **Thanks**

Thank you for checking out this project! I hope it's helpful.


