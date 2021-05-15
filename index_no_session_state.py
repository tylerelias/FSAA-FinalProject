import locale
from numpy import cos

import pandas as pd
import streamlit as st

import SessionState
from calculations.indexed import IndexLinked
from calculations.nonindexed import NonIndexedLinked
from text.text import Text

# Current inflation, look into making this value auto-updating
INFLATION = 4.6

# Set the currency to ISK
locale.setlocale(locale.LC_ALL, "is_IS.UTF-8")

# Used to keep track of the states
one=False  # Not needed?
two=False
three=False
four=False
principal=0
duration=0
interest=0.0
inflation=0.0
is_indexed=False
extra_payment=0
principal_list=0
payed_interest=0
monthly_payments=0
cost=0

def convert_to_isk(amount):
    return locale.currency(amount, grouping=True)


def make_same_size():
    len_principal = len(principal_list)
    len_saved = len(saved)

    # have to make principal and saved be the same size to plot
    tmp_saved = saved
    if len_saved < len_principal:
        for i in range(len_principal - len_saved):
            tmp_saved.append(0)
    return tmp_saved


def show_loan_saved_graph():
    st.write(f"# {Text.graph_title}")
    # we don't wanna update the actual saved array so we create a local variable
    saved = make_same_size()

    if saved != 0:
        df = pd.DataFrame({"Lán fyrir": principal_list, "Lán núna": saved})
    st.line_chart(df)


# Part of Step 3
def display_info(loan_type):
    isk = locale.currency(int(principal), grouping=True)
    # year month left
    year_left, month_left = format_time_saved(duration)

    st.markdown(Text.step_3)
    st.markdown(f"### {Text.loan_amount}: {isk}")
    st.markdown(f"### {Text.duration}: {duration}")
    if month_left > 0:
        st.markdown(
            f"### {Text.loan_duration} {year_left} {Text.years_and} {month_left} {Text.months} ")

    elif month_left <= 0:
        st.markdown(f"### {Text.loan_duration} {year_left} {Text.years}")

    st.markdown(f"### {Text.interest_rate}: {interest}%")
    with st.beta_expander(Text.wrong_input):
        st.markdown(f"{Text.if_wrong_input}")

    other_loan_type = ""
    _interest = 4.34
    if loan_type == "indexed":
        # calculate the chosen loan
        lt = IndexLinked(principal, duration,
                         interest, inflation, cost=cost)
        lt.index_calculation()
        # calculated the other loan to compare results
        other_loan_type = Text.non_indexed
        ot = NonIndexedLinked(principal, duration,
                              interest, cost=cost)
        ot.non_index_calculation()

    elif loan_type == "non_indexed":
        # calculate the chosen loan
        lt = NonIndexedLinked(principal, duration,
                              interest, cost=cost)
        lt.non_index_calculation()
        # calculated the other loan to compare results
        other_loan_type = Text.indexed
        ot = IndexLinked(principal, duration,
                         interest, _interest, cost=cost)
        ot.index_calculation()

    avg_monthly_payment = sum(lt.total_payment_list) / \
        len(lt.total_payment_list)
    interest_list_sum = sum(lt.interest_list)
    total_amount_paid = interest_list_sum + principal

    st.markdown(
        f"### {Text.monthly_payments}: {convert_to_isk(lt.total_payment_list[0])}")
    st.markdown(
        f"### {Text.total_interest_payment}: {convert_to_isk(sum(lt.interest_list))}")
    st.markdown(
        f"### {Text.total_amount_with_interest}: {convert_to_isk(total_amount_paid)}")
    st.markdown(
        f"### {Text.total_cost}: {convert_to_isk(lt.duration * lt.cost)}")
    st.markdown(
        f"### {Text.total_loan_payment}: {convert_to_isk(lt.get_total_payment())}")
    st.markdown(
        f"### Sama lán sem {other_loan_type} með {_interest}% verðbólgu: {convert_to_isk(ot.get_total_payment())}")

    principal_list = lt.principal_list
    payed_interest = lt.interest_list
    monthly_payments = avg_monthly_payment
    total_loan_amount = total_amount_paid

    # if(tegund == "indexed"):
    # st.markdown(f'{Text.stop_getting_ripped_off}')


def calculate_non_indexed():
    display_info("non_indexed")


def calculate_indexed():
    display_info("indexed")


# returns years, months
def format_time_saved(time):
    years = 0

    if time < 12:
        return years, time
    while time >= 12:
        time -= 12
        years += 1
    return years, time


def no_missing_parameters(loan_type):
    if(loan_type == 'Óverðtryggt'):
        return principal != 0 and duration != 0 and interest != 0.0 and cost != 0
    elif(loan_type == 'Verðtryggt'):
        return principal != 0 and duration != 0 and interest != 0.0 and inflation != 0.0 and inflation != 0 and cost != 0


if __name__ == "__main__":
    # The layout of the website
    # Header and introduction text for the website
    st.markdown(Text.header)
    st.markdown(Text.line)
    st.markdown(Text.intro_text)

    # The checkbox where the user selects the type of loan to fill out
    st.markdown(Text.step_1)
    loan_type = st.radio(
        "", (Text.none_selected, Text.non_indexed, Text.indexed), key="step_one"
    )
    with st.beta_expander(Text.n_idx_diff):
        st.markdown(Text.index_vs_nonindex)
    if loan_type == Text.none_selected:
        two = False
        three = False
        four = False
        

    ### step 2
    if loan_type != Text.none_selected:
        if loan_type == Text.non_indexed:
            is_indexed = False
        else:
            is_indexed = True
        # The form

        # Text for the site
        if loan_type == Text.non_indexed:
            st.markdown(Text.selected_non_indexed)
        elif loan_type == Text.indexed:
            st.markdown(Text.selected_indexed)

        st.markdown(Text.step_2)
        # Input fields
        # TODO: These values do not get updated when form is submitted again with changes
        # to the same field, but it does update if you change values in different fields?
        # this could be some Streamlit implementation problem
        
        principal = st.number_input(
            Text.loan_amount,
            value=principal,
            help=Text.amount_help,
            min_value=0,
            max_value=100000000000,
            step=1000000,
        )
        duration = st.number_input(
            Text.duration,
            value=duration,
            help=Text.duration_help,
            min_value=0,
            max_value=480,
            step=12,
        )
        interest = st.number_input(
            Text.interest_rate,
            value=interest,
            help=Text.interest_rate_help,
            min_value=-10.00,
            max_value=50.00,
            step=1.00,
        )
        cost = st.number_input(
            Text.cost,
            value=cost,
            help=Text.cost_help,
            min_value=-0,
            max_value=5000,
            step=10,
        )

        if loan_type == Text.indexed:
            inflation = st.number_input(
                Text.inflation_rate,
                value=inflation,
                help=Text.inflation_rate_help,
                min_value=-900000000.0,
                max_value=900000000.0,
                step=1.00,
            )
        # Submit the checkbox to get validated
        #submit = st.form_submit_button(Text.submit)
        # If user submits, or if user is in another state
        #if submit or two:
        if(no_missing_parameters(loan_type)):
            two = True

    ### step 3
    # For non-indexed case
    if two and is_indexed is False:
        with st.form("non_indexed_overview"):
            calculate_non_indexed()
            step_three_submit = st.form_submit_button(Text.btn_step4)
            if step_three_submit:
                print("inside nonindex")
                three = True

    # For indexed loan case
    if two and is_indexed is True:
        with st.form("indexed_overview"):
            calculate_indexed()
            step_three_submit = st.form_submit_button(Text.btn_step4)
            if step_three_submit:
                print("inside index")
                three = True

    ### step 4
    if three:
        st.markdown(Text.step_4)
        st.markdown(Text.pay_adjusted_rate)

        with st.beta_expander(Text.adj_fix_difference):
            st.markdown(Text.pay_adjusted_rate_example)

        extra_payment = st.number_input(
            Text.extra_payment,
            value=extra_payment,
            help=Text.extra_payment_help,
            min_value=0,
            max_value=1000000,
            step=10000,
        )

        if not is_indexed:
            nil = NonIndexedLinked(principal, duration, interest)
            nil.non_index_calculation()
            extra_amount = nil.calculation_extra_amount(principal)
            money_saved = nil.total_saved_from_extra_payment(extra_payment)
            year, month = format_time_saved(
                nil.time_saved_from_extra_payment(extra_payment)
            )
            # year month left
            months_shortened = duration - (year * 12 + month)
            year_left_now, month_left_now = format_time_saved(months_shortened)

            if extra_payment > 0:
                st.markdown(f"### {Text.monthly_extra_payment1} {convert_to_isk(extra_payment)} {Text.monthly_extra_payment2}")
                st.markdown(f"### {Text.money_saved}: {convert_to_isk(money_saved)}")
                st.markdown(f"### {Text.time_saved}: {year} {Text.years_and} {month} {Text.months} ")
                st.markdown(f"###")
                st.markdown(f"### {Text.total_loan}: {convert_to_isk(total_loan_amount - money_saved)}")
                if month_left_now > 0:
                    st.markdown(f"### {Text.loan_shortened_now} {year_left_now} {Text.years_and} {month_left_now} {Text.months} ")

                elif month_left_now <= 0:
                    st.markdown(f"### {Text.loan_shortened_now} {year_left_now} {Text.years}")
                saved = nil.principal_list
                show_loan_saved_graph()

            # TODO: Correctly add data to Pandas DF...
            # chart_data = pd.DataFrame(
            #     nil.principal_list, principal_list,
            #     columns=[Text.principal_downpay, 'hi']
            # )
            # st.line_chart(chart_data)

        elif is_indexed:
            ...
        st.markdown(Text.line)
