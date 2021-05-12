import streamlit as st
import pandas as pd
from print_helper import *
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
        #PrintVariables(l)
        DisplayInfo(lan_upphaed_milljonir, lans_timi_ar, vextir_ari, l.total_payment_list, l.principal_list, 0)
        
        n = ReFinance(repay, lan_upphaed_milljonir, lans_timi_ar, vextir_ari)
        DisplayInfo(lan_upphaed_milljonir, lans_timi_ar, vextir_ari, l.total_payment_list, l.principal_list, 1)

    elif(lan_typa == "Verðtryggt"):
        l = IndexLinked(lan_upphaed_milljonir, lans_timi_ar, vextir_ari, inflation)
        l.index_calculation()
        DisplayInfo(lan_upphaed_milljonir, lans_timi_ar, vextir_ari, l.total_payment_list, l.principal_list, -1)
    
    ## TODO: Add repayment to chart
    st.write("""# Lán afborganir""")
    st.line_chart(l.principal_list)
    #st.dataframe(l.total_payment_list)

