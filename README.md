# Gemini SQL Assistant

A Streamlit app that converts natural language to SQL using Google Gemini and runs queries on a SQLite database.

## Structure
- `app.py`: Main Streamlit app
- `modules/`: Helper modules (db_utils.py, gemini_utils.py, etc.)
- `db/`: SQLite database files
- `data/`: CSV and other data files
- `notebooks/`: Jupyter notebooks
- `static/`: Static files (images, etc.)
- `.env`: Environment variables (not tracked)
- `.gitignore`: Files to ignore in git
- `requirements.txt`: Python dependencies

## Usage
1. Add your Gemini API key to `.env`.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`
