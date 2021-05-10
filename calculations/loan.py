import pandas as pd

import indexed as idx


# Here logic for loan calculation is done

# indexed_loan Function
# Calculation of indexed loans (verðtryggð)
# @param: amount is the loan amount in ISK
# @param: duration is the length of the loan in months
# @param: interest is the current interest rate of the loan
# @param: inflation is the current inflation
# @return: [total amount paid, values to plot, ?]
def indexed_loan(amount, duration, interest, inflation):
    total_repaid = 0

    # TODO: Function call for calculations as done in: https://github.com/jackymallett/indexed/blob/master/ice.py
    # TODO: Returns bunch of data
    placeholder_list = idx.index_calculation(amount, duration, interest, inflation)

    plot_payments = pd.DataFrame({'placeholder': []})

    return total_repaid, plot_payments


# non_indexed_loan Function
# Calculation of non-indexed loans (overðtryggt)
# @param: amount is the loan amount in ISK
# @param: duration is the length of the loan in months
# @param: interest is the current interest rate of the loan
# @return: [total amount paid, values to plot, ?]
def non_indexed_loan(amount, duration, interest):
    total_repaid = 0
    plot_payments = pd.DataFrame({'placeholder': []})

    return total_repaid, plot_payments


if __name__ == '__main__':
    indexed_loan(0, 0, 0, 0)
    non_indexed_loan(0, 0, 0)
