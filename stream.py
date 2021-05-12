import streamlit as st
import pandas as pd
from calculations.indexed import IndexLinked
from calculations.nonindexed import NonIndexedLinked
from calculations.re_finance import ReFinance

lan_typa = st.sidebar.selectbox(
    'Lán?',
    ('Óverðtryggt', 'Verðtryggt')
)

if(lan_typa == "Óverðtryggt"):
    vextir_val = st.sidebar.radio(
        'Vextir á ári',
        ['3.44% breytilegir vextir', '4.20% fastir vextir í 3 ár']
    )

elif(lan_typa == "Verðtryggt"):
    vextir_val = st.sidebar.radio(
        'Vextir á ári',
        ['2.54% breytilegir vextir', '2.54% fastir vextir í 5 ár']
    )

inflation = st.sidebar.slider(
    'Inflation',
    1.0, 30.0, (4.3)
)

lanstimi = st.sidebar.slider(
    'Lánstími',
    5, 40, (40)
)

lan_upphaed = st.sidebar.slider(
    'Upphæð láns (Milljónir)',
    5.0, 200.0, (20.0)
)

repay = st.sidebar.slider(
    'Re finance (Þúsund)',
    5000, 1000000, (100000)
)

def GetHeaderLoanType(loan_type):
    # loan_type = 0 means óverðtryggt without additional money
    if(loan_type == 0):
        st.write("""# Lán án auka pening sett inn""")
    # loan_type = 1 means óverðtryggt with additional money invested
    elif(loan_type == 1):
        st.write("""# Lán með auka pening sett inn""")
    # otherwise we have verðtryggt lán
    else:
        st.write("""# Lán""")

def DisplayInfo(principal, loan_months, inflation, total_payment_list, principal_list=[], loan_type=0):
    GetHeaderLoanType(loan_type)
    st.write('lán = ', principal)
    st.write('mánuðir = ', loan_months)
    st.write('vextir sem bætast ofan á =', 0)
    st.write('Samtals greitt', sum(total_payment_list))


if __name__ == "__main__":
    lan_upphaed_milljonir = lan_upphaed*1000000
    lans_timi_ar = lanstimi * 12
    vextir_ari = float(vextir_val[:4].strip())
    
    if(lan_typa == "Óverðtryggt"):
        l = NonIndexedLinked(lan_upphaed_milljonir, lans_timi_ar, vextir_ari)
        l.non_index_calculation()
        DisplayInfo(lan_upphaed_milljonir, lans_timi_ar, vextir_ari, l.total_payment_list, l.principal_list, 0)
        
        n = ReFinance(repay, lan_upphaed_milljonir, lans_timi_ar, vextir_ari)
        DisplayInfo(lan_upphaed_milljonir, lans_timi_ar, vextir_ari, l.total_payment_list, l.principal_list, 1)

    elif(lan_typa == "Verðtryggt"):
        l = IndexLinked(lan_upphaed_milljonir, lans_timi_ar, vextir_ari, inflation)
        l.index_calculation()
        DisplayInfo(lan_upphaed_milljonir, lans_timi_ar, vextir_ari, l.total_payment_list, l.principal_list, -1)
    
    #PrintVariables(l)
    ## TODO: Add repayment to chart
    st.write("""# Lán afborganir""")
    st.line_chart(l.principal_list)
    #st.dataframe(l.total_payment_list)


# temporary variable to understand what is happening
def PrintVariables(l):
    print(f'Principal {l.principal}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Duration {l.duration}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Interest {l.interest}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Inflation {l.inflation}')
    print('============================')
    print('============================')
    print('============================')
    print(f'CPI {l.CPI}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Cost {l.cost}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Inflation index list {l.inflation_index_list}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Annuity factor list {l.annuity_factor_list}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Principal list {l.principal_list}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Payment list {l.payment_list}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Interest list {l.interest_list}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Payment of capital {l.payment_of_capital_list}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Step {l.step}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Total payment list {l.total_payment_list}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Monthly interest {l.monthly_interest}')
    print('============================')
    print('============================')
    print('============================')
    print(f'Monthly inflation {l.monthly_inflation}')
