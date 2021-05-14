import locale

import streamlit as st
import SessionState

from calculations.indexed import IndexLinked
from calculations.nonindexed import NonIndexedLinked
from text.text import Text

# Set the currency to ISK
locale.setlocale(locale.LC_ALL, 'is_IS.UTF-8')

# Used to keep track of the states
ss = SessionState.get(
    one=False,  # Not needed?
    two=False,
    three=False,
    four=False,
    principal=0,
    duration=0,
    interest=0.0,
    inflation=0.0,
    is_indexed=False,
    extra_payment=0
)


def loan_text_input():
    ss.principal = st.number_input(
        Text.loan_amount,
        value=ss.principal,
        help=Text.amount_help,
        min_value=0,
        max_value=100000000000,
        step=1000000
    )
    ss.duration = st.number_input(
        Text.duration,
        value=ss.duration,
        help=Text.duration_help,
        min_value=0,
        max_value=480,
        step=12
    )
    ss.interest = st.number_input(
        Text.interest_rate,
        value=ss.interest,
        help=Text.interest_rate_help,
        min_value=-10.00,
        max_value=50.00,
        step=1.00
    )


def step_one():
    # The checkbox where the user selects the type of loan to fill out
    st.markdown(Text.step_1)
    loan_type = st.radio(
        '',
        (Text.none_selected, Text.non_indexed, Text.indexed),
        key='step_one'
    )
    with st.beta_expander(Text.n_idx_diff):
        st.markdown("""
            TODO: Text
            """)
    if loan_type == Text.none_selected:
        ss.two = False
        ss.three = False
        ss.four = False

    return loan_type


def step_two(loan_type):
    if loan_type != Text.none_selected:
        if loan_type == Text.non_indexed:
            ss.is_indexed = False
        else:
            ss.is_indexed = True
        # The form
        with st.form(loan_type):
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
            loan_text_input()
            if loan_type == Text.indexed:
                ss.inflation = st.number_input(
                    Text.inflation_rate,
                    value=ss.inflation,
                    help=Text.inflation_rate_help,
                    min_value=-900000000.0,
                    max_value=900000000.0,
                    step=1.00
                )
            # Submit the checkbox to get validated
            submit = st.form_submit_button(Text.submit)
            # If user submits, or if user is in another state
            if submit or ss.two:
                ss.two = True


def step_three():
    # For non-indexed case
    if ss.two and ss.is_indexed is False:
        with st.form("non_indexed_overview"):
            calculate_non_indexed(ss.principal, ss.interest, ss.duration)
            step_three_submit = st.form_submit_button(Text.btn_step4)
            if step_three_submit:
                ss.three = True

    # For indexed loan case
    if ss.two and ss.is_indexed is True:
        with st.form("indexed_overview"):
            calculate_indexed(ss.principal, ss.interest, ss.duration, ss.inflation)
            step_three_submit = st.form_submit_button(Text.btn_step4)
            if step_three_submit:
                ss.three = True


def step_four():
    if ss.three:
        st.markdown(Text.step_4)
        payment_option = st.radio(
            '',
            (Text.none_selected, Text.radio_pay_fixed_rate, Text.radio_pay_adjusted_rate)
        )

        with st.beta_expander(Text.adj_fix_difference):
            st.markdown("""
            TODO: Text
            """)

        if payment_option == Text.radio_pay_fixed_rate:
            pay_fixed_rate()

        if payment_option == Text.radio_pay_adjusted_rate:
            pay_adjusted_rate()


def pay_fixed_rate():
    st.markdown(Text.pay_fixed_rate)
    st.markdown(Text.pay_fixed_rate_example)
    ss.extra_payment = st.number_input(
        Text.extra_payment,
        value=ss.extra_payment,
        help=Text.extra_payment_help,
        min_value=0,
        max_value=1000000,
        step=10000
    )

    if not ss.is_indexed:
        nil = NonIndexedLinked(ss.principal, ss.duration, ss.interest)
        nil.non_index_calculation()
        saved = nil.total_saved_from_extra_payment(ss.extra_payment)

        st.write("monthly extra payment: ", convert_to_isk(ss.extra_payment))
        st.write('money saved: ', convert_to_isk(saved))
        st.write('times saved: ', nil.time_saved_from_extra_payment(ss.extra_payment))

    st.markdown(Text.line)


def pay_adjusted_rate():
    st.markdown(Text.pay_adjusted_rate)
    st.markdown(Text.pay_adjusted_rate_example)


def convert_to_isk(amount):
    return locale.currency(amount, grouping=True)


# Part of Step 3
def display_info(tegund, principal, interest, duration, inflation=4.3):
    isk = locale.currency(int(principal), grouping=True)
    _interest = float(interest)
    _duration = int(duration)

    st.markdown(Text.step_3)
    st.markdown(f'### {Text.loan_amount}: {isk}')
    st.markdown(f'### {Text.duration}: {_duration}')
    st.markdown(f'### {Text.interest_rate}: {_interest}%')
    st.markdown(f'*{Text.if_wrong_input}*')

    if tegund == "indexed":
        _inflation = float(inflation)
        lt = IndexLinked(int(principal), _duration, _interest, _inflation)
        lt.index_calculation()
    elif tegund == "non_indexed":
        lt = NonIndexedLinked(int(principal), _duration, _interest)
        lt.non_index_calculation()

    st.markdown(
        f'### {Text.monthly_payments}: {convert_to_isk(lt.total_payment_list[0])}')
    st.markdown(
        f'### {Text.total_loan_payment}: {convert_to_isk(sum(lt.total_payment_list))}')
    st.markdown(
        f'### {Text.total_interest_payment}: {convert_to_isk(sum(lt.interest_list))}')

    # if(tegund == "indexed"):
    # st.markdown(f'{Text.stop_getting_ripped_off}')


def calculate_non_indexed(principal, interest, duration):
    display_info("non_indexed", principal, interest, duration)


def calculate_indexed(principal, interest, duration, inflation):
    display_info("indexed", principal, interest, duration, inflation)


if __name__ == '__main__':
    # The layout of the website
    # Header and introduction text for the website
    st.markdown(Text.header)
    st.markdown(Text.line)
    st.markdown(Text.intro_text)

    loan_type = step_one()
    step_two(loan_type)
    step_three()
    step_four()
