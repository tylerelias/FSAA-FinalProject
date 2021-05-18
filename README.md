# Loan calculator



### Installing

Start by creating a virtual environment in the root directory of the project

```bash
python -m venv .venv
```

Activate the virtual environment

Windows
```bash
. .venv/Scripts/activate
```
Linux
```bash
. .venv/bin/activate
```

Installed the required packages
```bash
pip install -r requirements.txt
```

Run the project using streamlit
```bash
streamlit run index.py
```

You can now view the web app in your browser!

### Info
index.py holds the frontend code

calculations/ holds all loan calculations

if streamlit run gives a weird error in the terminal, try deleting the credentials.toml file located in your streamlit directory (~/.streamlit by default)
