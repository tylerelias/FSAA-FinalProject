# The calculations for indexed linked loans (verðtryggð)
# Credit goes to Jacky Mallett for providing the formula: https://github.com/jackymallett/indexed

"""
# Set font characteristics
rcParams['font.family']   ='Courier'
rcParams['axes.labelsize']= '10'
rcParams['font.size']     = '11'

# Calculate loan      

duration  = 480
principal = 200000

# 

J = float(sys.argv[1])/12			# Monthly interest
N = duration
P = principal

capital  = []
interest = []
payment  = []
step     = []
princ    = []

M = P * (J/(1 - pow(1 + J, N * -1)))
for i in range(1, duration+1):

    H = P * J		# Monthly Interest
    C = M - H       # Capital repayment
    Q = P - C       # New capital balance

    capital.append(C)
    interest.append(H)
    payment.append(M)
    step.append(i)
    princ.append(P)

    P = Q
"""

import matplotlib.pyplot as plt


class IndexLinked:
    def __init__(self, principal, duration, interest, inflation, cost=130):
        self.principal = principal
        self.duration = duration
        self.interest = interest / 100
        self.inflation = inflation / 100
        self.CPI = 100
        self.cost = cost

        self.inflation_index_list = []
        self.annuity_factor_list = []
        self.principal_list = []
        self.payment_list = []
        self.interest_list = []
        self.payment_of_capital_list = []
        self.step = []
        self.total_payment_list = []

        self.monthly_interest = self.interest / 12
        self.monthly_inflation = pow(1 + self.inflation, 1 / 12) - 1

    def index_calculation(self):

        for i in range(1, self.duration + 1):
            if i == 1:
                inflation_index = self.CPI + self.CPI * self.monthly_inflation
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration)
                )
                principal = self.principal * inflation_index / self.CPI

            else:
                inflation_index += inflation_index * self.monthly_inflation

                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration - (i - 1))
                )
                principal = (principal - capital_payment) * (
                    inflation_index / self.inflation_index_list[i - 2]
                )
            payment = principal / annuity_factor
            interest = principal * self.monthly_interest
            capital_payment = payment - interest
            total_payment = payment + self.cost

            self.inflation_index_list.append(inflation_index)
            self.annuity_factor_list.append(annuity_factor)
            self.principal_list.append(principal)
            self.payment_list.append(payment)
            self.interest_list.append(interest)
            self.payment_of_capital_list.append(capital_payment)
            self.total_payment_list.append(total_payment)
            self.step.append(i)

    def _graph(self):
        plt.plot(self.step, self.principal_list)
        plt.show()


if __name__ == "__main__":
    l = IndexLinked(40000000, 40 * 12, 2.54, 4.3)
    l.index_calculation()
    l._graph()
