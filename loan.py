loan_amount = 19550000
la = loan_amount
years = 40
years_in_months = years*12
percentage = 3.44/100

amount = 0
for i in range(years):
    loan_year_amount = loan_amount/years
    print(f"year {i}, loan payment {loan_year_amount}")
    addition = loan_year_amount * percentage
    print(f"percentage increase {addition}")
    percentage_added = loan_year_amount + addition
    print(f"percentage added {percentage_added}")
    loan_months = percentage_added/12
    print(f"per month {loan_months}")
    loan_amount = loan_amount - loan_months
    amount += loan_months
    
print(f"total to add {amount}")
total = la+amount
print(f"original loan {la} + added {amount} = {total}")