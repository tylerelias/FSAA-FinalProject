import streamlit as st
import pandas as pd

loan_amount = 19550000
la = loan_amount
years = 40
years_in_months = years*12
percentage = 3.44/100

amount = 0
for i in range(years):
    loan_year_amount = loan_amount/years
    print(f"year {i}, loan payment {loan_year_amount}")
    addition = loan_year_amount * percentage
    print(f"percentage increase {addition}")
    percentage_added = loan_year_amount + addition
    print(f"percentage added {percentage_added}")
    loan_months = percentage_added/12
    print(f"per month {loan_months}")
    loan_amount = loan_amount - loan_months
    amount += loan_months

st.write("""
# Lán verð
""")
add_selectbox = st.sidebar.selectbox(
    'Lán?',
    ('Óverðtryggt', 'Verðtryggt')
)
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    '',
    0.0, 100.0, (25.0, 75.0)
)

#print(f"total to add {amount}")
total = la+amount
#print(f"original loan {la} + added {amount} = {total}")
df = pd.DataFrame({'num_legs': [20000, 40000, 80000, 0, 40000, 44000, 55000, 350000]})
st.line_chart(df)