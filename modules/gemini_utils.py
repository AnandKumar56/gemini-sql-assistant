import google.generativeai as genai

def get_gemini_sql(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt[0], question])
    sql_query = response.text.strip()
    sql_query = sql_query.replace("```sql", "").replace("```", "")
    return sql_query

def explain_sql_query(query):
    explain_prompt = f"Explain this SQL query step-by-step in simple terms:\n{query}"
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(explain_prompt)
    return response.text.strip()
