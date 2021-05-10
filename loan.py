import streamlit as st
import pandas as pd

#loan_amount = 19550000
loan_amount = 16100000
la = loan_amount
years = 40
years_in_months = years*12
percentage = 3.44/100

amount = 0

print(loan_amount)
copy_years = years
for i in range(copy_years):
    # 16.100.000 => 402500 per year (first year)
    print(f"year: {i+1}")
    loan_per_year = loan_amount/years
    print(f"loan for year: {loan_per_year}")
    loan_payment_for_year = loan_per_year*percentage
    print(f"loan interest: {loan_payment_for_year}")
    loan_increase = loan_per_year+loan_payment_for_year
    print(f"loan for year with interest: {loan_increase}")
    # loan shrinks after paying for a year
    loan_amount = loan_amount-loan_increase
    # Years shrink so the loan_per_year can be calculated from remaining years
    years = years-1
    print(f"loan left: {loan_amount}")
    amount += loan_increase
   

add_selectbox = st.sidebar.selectbox(
    'Lán?',
    ('Óverðtryggt', 'Verðtryggt')
)
# Add a slider to the sidebar:
#upphaed_lans = st.sidebar.slider(
 #   'Fasteignamat',
  #  0, 140000000, (16100000)
#)

lanstimi = st.sidebar.slider(
    'Lánstími',
    5, 40, (40)
)

vextir_ari = st.sidebar.selectbox(
    'Vextir á ári',
    ('3,44% breytilegir vextir', '4,20% fastir vextir í 3 ár')
)

total = la+amount

#add_slider = st.sidebar.slider(
 #   'Fasteignamat',
 #   23000000, 200000000, (23000000)
#´)

st.write("""#Lán""")
st.write('lán = ', la)
st.write('vextir sem bætast ofan á =', amount)
st.write('Samanlagt ', total)

st.write("""
# Lán afborganir
""")
df = pd.DataFrame({'num_legs': [20000, 40000, 80000, 0, 40000, 44000, 55000, 350000]})
st.line_chart(df)
