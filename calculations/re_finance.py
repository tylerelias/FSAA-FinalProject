import matplotlib.pyplot as plt
from calculations.indexed import IndexLinked
from calculations.nonindexed import NonIndexedLinked


class ReFinance:
    def __init__(
        self, refinance_cost, principal, duration, interest, inflation=4.3, cost=130
    ):
        self.refinance_cost = refinance_cost
        self.principal = principal
        self.duration = duration
        self.interest = interest / 100
        self.cost = cost
        self.inflation = inflation

        self.ind = IndexLinked(
            self.principal, self.duration, self.interest, self.inflation
        )
        self.non = NonIndexedLinked(self.principal, self.duration, self.interest)

        self._calculate()

    def _calculate(self):
        self.ind.index_calculation()
        self.non.non_index_calculation()

    def savings_from_refinancing(self):
        ...

    def repay_cost(self):
        ...


if __name__ == "__main__":
    n = ReFinance(200000, 40000000, 40 * 12, 3.44)
