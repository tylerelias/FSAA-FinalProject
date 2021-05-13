import matplotlib.pyplot as plt
from indexed import IndexLinked
from nonindexed import NonIndexedLinked
import numpy as np


class ReFinance:
    def __init__(
        self,
        refinance_cost,
        principal,
        duration,
        ind_interest,
        nonind_interest,
        inflation=4.3,
        cost=130,
    ):
        self.refinance_cost = refinance_cost
        self.principal = principal
        self.duration = duration
        self.ind_interest = ind_interest
        self.nonind_interest = nonind_interest
        self.cost = cost
        self.inflation = inflation

        self.ind = IndexLinked(
            self.principal, self.duration, self.ind_interest, self.inflation
        )
        self.non = NonIndexedLinked(self.principal, self.duration, self.nonind_interest)

        self._calculate()

    def _calculate(self):
        self.ind.index_calculation()
        self.non.non_index_calculation()

    # how much you save in total from refinancing from indexed to non indexed
    def savings_from_refinancing(self):
        return (
            self.ind.get_total_payment()
            - self.non.get_total_payment()
            - self.refinance_cost
        )

    # how long it takes to repay the refinance
    def time_to_repay(self):
        ind_payments = self.ind.total_payment_list
        nonind_payments = self.non.total_payment_list

        diff = [y - x for y, x in zip(ind_payments, nonind_payments)]

        cumsum = np.cumsum(diff)
        return np.where(cumsum > 0 + self.refinance_cost)[0][0]


if __name__ == "__main__":
    n = ReFinance(200000, 40000000, 40 * 12, 2.54, 3.44)

    print(n.time_to_repay())
