import streamlit as st
import pandas as pd
from calculations.indexed import IndexLinked

lan_typa = st.sidebar.selectbox(
    'Lán?',
    ('Óverðtryggt', 'Verðtryggt')
)

lanstimi = st.sidebar.slider(
    'Lánstími',
    5, 40, (40)
)

lan_upphaed = st.sidebar.slider(
    'Upphæð láns (Milljónir)',
    5.0, 200.0, (20.0)
)

vextir_ari = st.sidebar.radio(
    'Vextir á ári',
    ['3,44% breytilegir vextir', '4,20% fastir vextir í 3 ár']
)

inflation = st.sidebar.slider(
    'Inflation',
    1.0, 30.0, (4.3)
)

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

def DisplayInfo(principal, interest, inflation, cost=130, total_payments=[]):
    st.write("""# Lán""")
    st.write('lán = ', principal)
    st.write('mánuðir = ', interest)
    st.write('vextir sem bætast ofan á =', )
    st.write('Samanlagt ', cost)

    st.write("""# Lán afborganir""")
    st.line_chart(total_payments)


if __name__ == "__main__":
    milljon = 1000000
    #principal, duration, interest, inflation, cost
    vextir_ari_use = 3.44
    if(vextir_ari == "3,44% breytilegir vextir"):
        vextir_ari_use = 3.44
    elif(vextir_ari == "4,20% fastir vextir í 3 ár"):
        vextir_ari_use = 4.20
    l = IndexLinked(lan_upphaed*milljon, lanstimi * 12, vextir_ari_use, inflation)
    l.index_calculation()
    #l._graph()
    #print(l.total_payment_list)
    total_payments = l.total_payment_list
    #PrintVariables(l)
    DisplayInfo(lan_upphaed*milljon, lanstimi * 12, vextir_ari_use, inflation, l.principal_list)


#Total payment list 
# [133392.42361623913, 133860.78680864043, 134330.79610707852, 134802.45729694635, 135275.7761839701, 135750.75859428072, 136227.41037448565, 136705.73739174075, 137185.74553382257, 137667.44070920086, 138150.82884711112, 138635.9158976278, 139122.70783173732, 139611.21064141186, 140101.43033968282, 140593.37296071497, 141087.0445598807, 141582.45121383466, 142079.5990205884, 142578.49409958548, 143079.14259177685, 143581.55065969637, 144085.7244875368, 144591.67028122567, 145099.39426850196, 145608.90269899252, 146120.20184428914, 146633.29799802564, 147148.19747595553, 147664.90661602953, 148183.43177847366, 148703.7793458676, 149225.95572322322, 149749.96733806332, 150275.82064050087, 150803.5221033184, 151333.0782220475, 151864.49551504917, 152397.78052359354, 152932.93981194068, 153469.97996742156, 154008.90760051872, 154549.72934494793, 155092.45185773986, 155637.08181932173, 156183.62593359992, 156732.09092804225, 157282.48355376095, 157834.8105855954, 158389.0788221961, 158945.2950861079, 159503.46622385402, 160063.59910602056, 160625.70062734088, 161189.7777067805, 161755.83728762247, 162323.8863375524, 162893.93184874457, 163465.98083794798, 164040.0403465725, 164616.11744077594, 165194.2192115505, 165774.35277481045, 166356.52527147965, 166940.74386757935, 167527.01575431647, 168115.34814817208, 168705.74829099022, 169298.22345006707, 169892.78091824055, 170489.42801397966, 171088.1720814751, 171689.02049072925, 172291.98063764707, 172897.05994412725, 173504.26585815323, 174113.60585388524, 174725.08743175198, 175338.71811854336, 175954.5054675027, 176572.45705841988, 177192.5804977248, 177814.8834185807, 178439.37348097845, 179066.05837183053, 179694.94580506586, 180326.0435217246, 180959.3592900537, 181594.90090560218,