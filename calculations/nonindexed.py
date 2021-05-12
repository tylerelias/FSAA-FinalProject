import matplotlib.pyplot as plt


class NonIndexedLinked:
    """
    principal is the capital loan amount
    intereset is yearly in percentages (i.e. 4.34)
    duration is in months
    cost is monthly fee from the bank

    """

    def __init__(self, principal, duration, interest, cost=130):
        self.principal = principal
        self.duration = duration
        self.interest = interest / 100
        self.cost = cost

        self.principal_list = []
        self.payment_list = []
        self.interest_list = []
        self.payment_of_capital_list = []
        self.step = []
        self.total_payment_list = []
        self.annuity_factor_list = []

        self.monthly_interest = self.interest / 12

    def non_index_calculation(self):
        for i in range(1, self.duration + 1):
            # seperate calculation for initial step
            if i == 1:
                # annuity factor, necessary for index calculations
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration)
                )

                # calculated principal change per month
                principal = self.principal

            # every step after initial step, since they depend on previous values
            else:
                # annuity factor, necessary for index calculations
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration - (i - 1))
                )

                # calculated principal change per month
                principal = principal - capital_payment

            # monthly payment
            payment = principal / annuity_factor

            # how much of payment is payment of interests
            interest = principal * self.monthly_interest

            # how much of payment is payment of loan capital
            capital_payment = payment - interest

            # total payment, with monthly cost constant added
            total_payment = payment + self.cost

            # store value from each month for graphing and calculation purposes
            self.annuity_factor_list.append(annuity_factor)
            self.principal_list.append(principal)
            self.payment_list.append(payment)
            self.interest_list.append(interest)
            self.payment_of_capital_list.append(capital_payment)
            self.total_payment_list.append(total_payment)
            self.step.append(i)

    def calculation_extra_amount(self, amount):
        for i in range(1, self.duration + 1):
            # seperate calculation for initial step
            if i == 1:
                # annuity factor, necessary for index calculations
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration)
                )

                # calculated principal change per month
                principal = self.principal

                payment = principal / annuity_factor + amount

            # every step after initial step, since they depend on previous values
            else:
                # annuity factor, necessary for index calculations
                annuity_factor = (1 / self.monthly_interest) - 1 / (
                    self.monthly_interest
                    * pow(1 + self.monthly_interest, self.duration - (i - 1))
                )

                # calculated principal change per month
                principal = principal - capital_payment

            # how much of payment is payment of interests
            interest = principal * self.monthly_interest

            # how much of payment is payment of loan capital
            capital_payment = payment - interest

            # total payment, with monthly cost constant added
            total_payment = payment + self.cost

            # store value from each month for graphing and calculation purposes
            self.annuity_factor_list.append(annuity_factor)
            self.principal_list.append(principal)
            self.payment_list.append(payment)
            self.interest_list.append(interest)
            self.payment_of_capital_list.append(capital_payment)
            self.total_payment_list.append(total_payment)
            self.step.append(i)
            if principal < 0:
                break

    def _graph(self):
        plt.plot(self.step, self.principal_list)

    # total amount payed
    def get_total_payment(self):
        return sum(self.total_payment_list)



if __name__ == "__main__":

    l = NonIndexedLinked(
        40000000,
        40 * 12,
        3.44,
    )
    l.non_index_calculation()
    l._graph()

    print(sum(l.total_payment_list))
    print(l.interest_list)

    """k = NonIndexedLinked(
        40000000,
        40 * 12,
        3.44,
    )
    k.non_index_calculation_extra(50000)
    k._graph()

    # print(k.total_payment_list)
    print(len(k.total_payment_list))
    print(sum(l.total_payment_list))
    print(sum(k.total_payment_list))
    print(k.total_payment_list)
    """
