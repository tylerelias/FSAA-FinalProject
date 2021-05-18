# Mortgage Loan Repayment Calculator

When people take out loans they are often not aware how much extra cost follows the interest payments, it would be ideal that they would be able to see the hidden costs in a clear and effective way. Being able to get an estimate on how much money one would save by putting monthly down payments on the loan would also be a nice feature and encourage people to do so.

A calculator to show people how much they could save on their loans by doing monthly down payments in an easy and intuitive way to encourage them to attempt to pay their loans earlier than the loan contract suggests.

The end product will be a user-friendly website that will be openly accessible and with the aim of increasing financial awareness for the public.

## Backend

The backend will be taking care of the calculations of the loans and will take in the following parameters from a user:

- Loans (Grunnlán & Viðbótarlán)
- Loan amount
- Loan duration
- Interest rates
- Inflation (if verðtryggt)

The backend will need to be able to make the correct calculations to the two different types of loans: [verðtryggt](https://github.com/jackymallett/indexed) / óverðtryggt and:

- Estimate the ideal monthly payments into the loan (based on a person's income)
    - Estimate how much money is saved by paying into the loan
- Overview of estimated savings
- Overview of total payments made vs the original loan amount
- Give data that can be plotted
- User sets the current interest rates of its loan (depends on bank/institution & when loan was taken)

## Suggested Features

- Be able to modify specific monthly payments into a loan (Ragnar)
- Scrape the inflation rate from sedlabankinn.is?
- Suggest monthly payments base on a person's income (Steinar)
- Small & Simple wiki-like section
    - Recommend óverðtryggt lán by giving simple examples (this would be in a section of the website for those that want to read and get more informed)
    - Explain terms related to loans in a simple way:
        - verðtryggt vs óverðtryggt
        - stýrivextir seðlabankanns
        - fastir vs breytilegir vextir
        - how stýrivextir affects breytilegir vextir
- Be able to export the calculations to Excel/PDF file

### Programming Language & Framework

For the sake of simplicity and coding efficiency Python is desirable.

## Frontend

The frontend is what the user will be using a seeing. The explanations for the loans and things related to them will need to be user-friendly and easy to understand, even if the peron is not very informed about finance.

There should also be additional sections to explain the importance and benefits of making down payments into a loan.

### Homepage

- Toolbar
    - Home
        - Short & simple text about the site and how it works
        - The loan payment calculator will be here
    - Information
        - The small wiki-like section with more detailed information
    - About Us

### Programming Language & Framework

Javascript is looking like a candidate as the frontend programming language. React will most likely be used to design the website. None of these are final decision and can change in the future.

