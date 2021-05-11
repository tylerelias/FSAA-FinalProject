import matplotlib.pyplot as plt


class NonIndexedLinked:
    def __init__(self, principal, duration, interest, cost=130):
        self.principal = principal
        self.duration = duration
        self.interest = interest / 100
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

    def non_index_calculation(self):
        for i in range(1, self.duration + 1):
            if i == 1:
                inflation_index = self.CPI + self.CPI
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                        self.monthly_interest
                        * pow(1 + self.monthly_interest, self.duration)
                )
                principal = self.principal * inflation_index / self.CPI

            else:

                annuity_factor = (1 / self.monthly_interest) - 1 / (
                        self.monthly_interest
                        * pow(1 + self.monthly_interest, self.duration - (i - 1))
                )
                principal = (principal - capital_payment)

            payment = principal / annuity_factor
            interest = principal * self.monthly_interest
            capital_payment = payment - interest
            total_payment = payment + self.cost

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
    l = NonIndexedLinked(40000000, 40 * 12, 3.44,)
    l.non_index_calculation()
    print(l.total_payment_list)
    l._graph()
