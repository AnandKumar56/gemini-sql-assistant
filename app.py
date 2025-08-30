import sqlite3
import streamlit as st
import os
import datetime
import pandas as pd
from dotenv import load_dotenv
from modules.db_utils import read_sql_query, get_db_schema
from modules.gemini_utils import get_gemini_sql, explain_sql_query
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in your .env file.")
genai.configure(api_key=GEMINI_API_KEY)

# Professional 6-Part Prompt for Gemini
prompt = ["""
# 1. Context:
You are helping a user interact with a SQLite database using natural language.

# 2. Role:
You are an expert SQL assistant who converts English questions into SQLite queries.

# 3. Constraints:
- Use only SQLite syntax.
- Target database: Naresh_it_employee1.
- Table: Naresh_it_employee1.
- Columns: employee_name (text), employee_role (text), employee_salary (float).
- Do not use backticks (`), triple quotes (```), or semicolons.
- Keep SQL readable and correct.

# 4. Instructions:
- Translate the user's question into a valid SQL query.
- Be precise in filtering, grouping, or sorting.
- Make sure the column names and logic match the schema.

# 5. Few-shot Examples:

Q: How many employees are there?
A: SELECT COUNT(*) FROM Naresh_it_employee1

Q: Show all Data Engineers
A: SELECT * FROM Naresh_it_employee1 WHERE employee_role = 'Data Engineer'

Q: Who earns more than 60000?
A: SELECT * FROM Naresh_it_employee1 WHERE employee_salary > 60000

Q: Who earns the highest salary?
A: SELECT * FROM Naresh_it_employee1 ORDER BY employee_salary DESC LIMIT 1

# 6. Chain of Thought:
First, understand the user’s question and identify relevant filters or conditions.  
Then map to the appropriate SQL clause (e.g., SELECT, WHERE, GROUP BY, ORDER BY).  
Finally, return the correct and clean SQL query.

Now generate the SQL query for this question:
"""]


# Streamlit App UI
st.set_page_config(page_title="LLM SQL Assistant")

# --- MENU BAR ---

# Sidebar with Menu heading and buttons
st.sidebar.markdown("## Menu")
menu_home = st.sidebar.button("Home")
menu_history = st.sidebar.button("History")
menu_about = st.sidebar.button("About")

# Determine which menu is active
if 'active_menu' not in st.session_state:
    st.session_state['active_menu'] = 'Home'
if menu_home:
    st.session_state['active_menu'] = 'Home'
if menu_history:
    st.session_state['active_menu'] = 'History'
if menu_about:
    st.session_state['active_menu'] = 'About'
menu = st.session_state['active_menu']


# Simple toast messages (auto-disappear)
def show_toast(msg, type_="info"):
    # st.toast is available in Streamlit >=1.32
    try:
        st.toast(msg, icon="✅" if type_=="success" else ("⚠️" if type_=="warning" else ("❌" if type_=="error" else "ℹ️")))
    except Exception:
        # fallback
        if type_ == "success":
            st.success(msg)
        elif type_ == "error":
            st.error(msg)
        elif type_ == "warning":
            st.warning(msg)
        else:
            st.info(msg)


# Show toasts for DB/API connectivity (only once per session)
if 'shown_toasts' not in st.session_state:
    st.session_state['shown_toasts'] = False
if not st.session_state['shown_toasts']:
    db_connected = False
    api_connected = False
    try:
        conn = sqlite3.connect(os.path.join("db", "Naresh_it_employee1.db"))
        conn.close()
        db_connected = True
    except Exception as e:
        show_toast(f"SQL not connected: {e}", "error")
    if db_connected:
        show_toast("Database connected successfully!", "success")
    try:
        _ = genai.GenerativeModel('gemini-2.0-flash')
        api_connected = True
    except Exception as e:
        show_toast(f"API not connected: {e}", "error")
    if api_connected:
        show_toast("Gemini API ready!", "success")
    st.session_state['shown_toasts'] = True

if menu == "Home":
    st.title("Gemini SQL Assistant")
    st.write("Ask questions in English. Get SQL queries and results instantly!")

    question = st.text_input("Enter your question:")

    with st.expander("Try These Examples"):
        st.markdown("""
        - List all employees.
        - Show only Data Scientists.
        - Who earns more than 60,000?
        - Count of Data Engineers?
        - Highest salary employee?
        - Provide the average salary based on job role.
        """)

    run_btn = st.button("Run")
    if run_btn:
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            sql_query = get_gemini_sql(question, prompt)
            st.subheader("Generated SQL Query:")
            st.code(sql_query, language="sql")
            result, columns = read_sql_query(sql_query, os.path.join("db", "Naresh_it_employee1.db"))
            # Save to history CSV
            history_row = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "question": question,
                "sql_query": sql_query,
                "result": str(result)
            }
            hist_file = os.path.join("data", "search_history.csv")
            if os.path.exists(hist_file) and os.path.getsize(hist_file) > 0:
                df_hist = pd.read_csv(hist_file)
                df_hist = pd.concat([df_hist, pd.DataFrame([history_row])], ignore_index=True)
            else:
                df_hist = pd.DataFrame([history_row])
            df_hist.to_csv(hist_file, index=False)

            if result and "SQL Error" in result[0]:
                st.error(f"Error: {result[0][1]}")
            else:
                st.subheader("Query Result:")
                df = pd.DataFrame(result, columns=columns)
                st.dataframe(df, use_container_width=True)
                with st.expander("Gemini Explains the SQL"):
                    explanation = explain_sql_query(sql_query)
                    st.write(explanation)

    schema_btn = st.button("View DB Schema")
    if schema_btn:
        st.subheader("Database Schema")
        schema = get_db_schema(os.path.join("db", "Naresh_it_employee1.db"))
        if "Error" in schema:
            st.error(schema["Error"])
        else:
            for tname, cols in schema.items():
                st.markdown(f"### Table: `{tname}`")
                df_schema = pd.DataFrame(cols, columns=["Field Name", "Type"])
                st.dataframe(df_schema, use_container_width=True)

elif menu == "History":
    st.title("Search History")
    hist_file = os.path.join("data", "search_history.csv")
    if os.path.exists(hist_file) and os.path.getsize(hist_file) > 0:
        df_hist = pd.read_csv(hist_file)
        st.dataframe(df_hist, use_container_width=True)
        st.download_button("Download History as CSV", data=df_hist.to_csv(index=False), file_name="search_history.csv")
    else:
        st.info("No search history found.")

elif menu == "About":
    st.title("About This Application")
    st.markdown("""
    **Gemini SQL Assistant** is an AI-powered tool that converts natural language questions into SQL queries for your SQLite database. It uses Google Gemini LLM for query generation and explanation, and provides:
    - Instant SQL generation and execution
    - Search history tracking
    - Database schema viewer
    - Toast notifications for connectivity
    
    _Developed for demonstration and learning purposes._
    """)
