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
        self.verdbaetur_list = []

        self.monthly_interest = self.interest / 12
        self.monthly_inflation = pow(1 + self.inflation, 1 / 12) - 1

    def index_calculation(self):

        # For each month in time period
        for i in range(1, self.duration + 1):
            # seperate calculation for initial step
            if i == 1:
                # inflation index, necessary for index calculations
                inflation_index = self.CPI + self.CPI * self.monthly_inflation

                # annuity factor, necessary for index calculations
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration)
                )

                # calculated principal change per month
                principal = self.principal * inflation_index / self.CPI
                verdbaetur = self.principal * self.monthly_inflation

            # every step after initial step, since they depend on previous values
            else:
                # inflation index, necessary for index calculations
                inflation_index += inflation_index * self.monthly_inflation

                # annuity factor, necessary for index calculations
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration - (i - 1))
                )

                # calculated principal change per month
                principal = (principal - capital_payment) * (
                    inflation_index / self.inflation_index_list[i - 2]
                )
                verdbaetur = (
                    self.principal_list[i - 2] - self.payment_of_capital_list[i - 2]
                ) * self.monthly_inflation

            # monthly payment
            payment = principal / annuity_factor

            # how much of payment is payment of interests
            interest = principal * self.monthly_interest

            # how much of payment is payment of loan capital
            capital_payment = payment - interest

            # total payment, with monthly cost constant added
            total_payment = payment + self.cost

            # store value from each month for graphing and calculation purposes
            self.inflation_index_list.append(inflation_index)
            self.annuity_factor_list.append(annuity_factor)
            self.principal_list.append(principal)
            self.payment_list.append(payment)
            self.interest_list.append(interest)
            self.payment_of_capital_list.append(capital_payment)
            self.total_payment_list.append(total_payment)
            self.step.append(i)
            self.verdbaetur_list.append(verdbaetur)

    def _clear_buffer(self):
        self.inflation_index_list = []
        self.annuity_factor_list = []
        self.principal_list = []
        self.payment_list = []
        self.interest_list = []
        self.payment_of_capital_list = []
        self.step = []
        self.total_payment_list = []

    # calculates the loan table with extra month added, and savings reinvested
    def calc_with_extraamount(self, amount):
        self._clear_buffer()

        self.index_calculation()
        normal_total_payments = self.total_payment_list

        self._clear_buffer()
        # For each month in time period
        for i in range(1, self.duration + 1):
            # seperate calculation for initial step
            if i == 1:
                # inflation index, necessary for index calculations
                inflation_index = self.CPI + self.CPI * self.monthly_inflation

                # annuity factor, necessary for index calculations
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration)
                )

                # calculated principal change per month
                principal = self.principal * inflation_index / self.CPI
                verdbaetur = self.principal * self.monthly_inflation

            # every step after initial step, since they depend on previous values
            else:
                # inflation index, necessary for index calculations
                inflation_index += inflation_index * self.monthly_inflation

                # annuity factor, necessary for index calculations
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration - (i - 1))
                )

                # calculated principal change per month
                principal = (principal - capital_payment) * (
                    inflation_index / self.inflation_index_list[i - 2]
                )

                verdbaetur = (
                    self.principal_list[i - 2] - self.payment_of_capital_list[i - 2]
                ) * self.monthly_inflation

            # monthly payment
            # payment = principal / annuity_factor

            payment = normal_total_payments[i - 1] + amount

            # how much of payment is payment of interests
            interest = principal * self.monthly_interest

            # how much of payment is payment of loan capital
            capital_payment = payment - interest

            # total payment, with monthly cost constant added
            total_payment = payment + self.cost

            # store value from each month for graphing and calculation purposes
            self.inflation_index_list.append(inflation_index)
            self.annuity_factor_list.append(annuity_factor)
            self.principal_list.append(principal)
            self.payment_list.append(payment)
            self.interest_list.append(interest)
            self.payment_of_capital_list.append(capital_payment)
            self.total_payment_list.append(total_payment)
            self.step.append(i)
            self.verdbaetur_list.append(verdbaetur)

            if principal < 0:
                break

    def _graph(self):
        plt.plot(self.step, self.principal_list)

    # total amount payed
    def get_total_payment(self):
        return sum(self.total_payment_list)

    # highest loan capital point
    def get_loan_highpoint(self):
        return max(self.principal_list)

    def total_saved_from_extra_payment(self, amount):
        self._clear_buffer()
        self.index_calculation()
        norm = sum(self.total_payment_list)
        self._clear_buffer()

        self.calc_with_extraamount(amount)
        ex = sum(self.total_payment_list)

        return norm - ex

    def time_saved_from_extra_payment(self, amount):
        self._clear_buffer()
        self.index_calculation()
        norm = len(self.total_payment_list)
        self._clear_buffer()

        self.calc_with_extraamount(amount)
        ex = len(self.total_payment_list)

        return norm - ex

    def get_total_indexation(self):
        return sum(self.verdbaetur_list)


if __name__ == "__main__":
    lt = IndexLinked(40000000, 40 * 12, 2.54, 4.3, cost=130)
    lt.index_calculation()

    print(lt.get_total_indexation())
