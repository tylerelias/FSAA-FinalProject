# FSAA-FinalProject

## Mortgage Loan Repayment Calculator

When people take out loans they often are not aware how much extra cost follows the interest payments. It would be ideal that they would be able to see the hidden costs in a clear and effective way. Being able to get an estimate on how much money one would save by putting monthly down payments on the loan would also be a nice feature and encourage people to do so.

A calculator to show people how much they could save on their loans by doing monthly down payments in a easy and intuitive way to encourage them to attempt to pay their loans earlier than the loan contract suggests.

The end product will be a user-friendly website that will be openly accessable and with the aim of increasing financial awareness for the general public.

## Backend

The backend will be taking care of the calculations of the loans and will take in the following parameters from a user:

- Loans (Grunnlán & Viðbótarlán)
- Loan amount
- Loan duration
- Interest rates
- Inflation (if verðtryggt)

The backend will need to be able to make the correct calculations to the two different types of loans: verðtryggt / óverðtryggt and:

- Estimate the monthly payments for those loans
- Estimate what payments will be if there are are monthly payments made into the loan
- Overview of estimated savings
- Overview of total payments made vs the original loan amount
- Give data that can be plotted

### Programming Language & Framework

For the sake of simplicity and efficiency Python is desirable.

## Frontend

The frontend is what the user will be using a seeing. The explanations for the loans and things related to them will need to be user-friendly and easy to understand, even if the peron is not very informed about finance.

There should also be additional sections to explain the importance and benefits of making down payments into a loan.

### Programming Language & Framework

Javascript is looking like a candidate as the frontend programming language. React will most likely be used to design the website. None of these are final decision and can change in the future.

