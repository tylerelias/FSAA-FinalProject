import locale

import streamlit as st
import SessionState

from calculations.indexed import IndexLinked
from calculations.nonindexed import NonIndexedLinked
from text.text import Text

locale.setlocale(locale.LC_ALL, 'is_IS.UTF-8')


def validate_input(principal, interest, duration, inflation='0.0'):
    if not principal.isnumeric() or int(principal) < 1:
        return False
    if not duration.isnumeric() or int(duration) < 1:
        return False
    if not interest.replace('.', '', 1).isdigit() or float(interest) < 0:
        return False
    if not inflation.replace('.', '', 1).isdigit():
        return False
    return True


def step_one():
    # The checkbox where the user selects the type of loan to fill out
    st.markdown(Text.step_1)
    loan_type = st.radio(
        '',
        (Text.none_selected, Text.non_indexed, Text.indexed),
        key='step_one'
    )
    return loan_type


def step_two(loan_type):
    principal = '0'
    duration = '0'
    interest = '0.0'
    inflation = '0.0'
    is_indexed = False
    if loan_type != Text.none_selected:
        principal = st.text_input(
            Text.loan_amount,
            "40000000",
            help=Text.amount_help
        )
        duration = st.text_input(
            Text.duration,
            "300",
            help=Text.duration_help
        )
        interest = st.text_input(
            Text.interest_rate,
            "3.3",
            help=Text.interest_rate_help
        )
    # non-indexed loans
    if loan_type == Text.non_indexed:
        # The form
        with st.form("non_indexed"):
            # Text for the site
            st.markdown(Text.selected_non_indexed)
            st.markdown(Text.step_2)
            # Print out the various stats

            # Submit the checkbox to get validated
            submit = st.form_submit_button(Text.submit)

            if submit or is_step_two.checkboxed:
                if validate_input(principal, interest, duration):
                    is_step_two.checkboxed = True
                else:
                    # TODO: Fix to make a proper Wrong Value message
                    is_step_two.checkboxed = False
                    st.markdown("## Illegal input")

    # Second step - indexed
    if loan_type == Text.indexed:
        is_indexed = True
        with st.form("indexed"):
            st.markdown(Text.selected_indexed)
            st.markdown(Text.step_2)

            inflation = float(st.text_input(
                Text.inflation_rate,
                "4.6",
                help=Text.inflation_rate_help
            ))

            submit = st.form_submit_button(Text.submit)
            if submit:
                if validate_input(principal, interest, duration, inflation):
                    is_step_two.checkboxed = True
                else:
                    # TODO: Fix to make a proper Wrong Value message
                    is_step_two.checkboxed = False
                    st.markdown("## Illegal input")

    return principal, interest, duration, inflation, is_indexed


def step_three(principal, interest, duration, inflation, is_indexed):
    # For non-indexed case
    if is_step_two.checkboxed and is_indexed is False:
        with st.form("non_indexed_overview"):
            calculate_non_indexed(principal, interest, duration)
            step_three_submit = st.form_submit_button(Text.btn_step4)
            # st.write(is_step_three.checkboxed)
            if step_three_submit:
                is_step_three.checkboxed = True

    # For indexed loan case
    if is_step_two.checkboxed and is_indexed is True:
        with st.form("indexed_overview"):
            calculate_indexed(principal, interest, duration, inflation)
            step_three_submit = st.form_submit_button(Text.btn_step4)
            if step_three_submit:
                is_step_three.checkboxed = True


def step_four():
    # st.write(is_step_three.checkboxed)
    if is_step_three.checkboxed:
        with st.form("step_four"):
            st.markdown(Text.step_4)
            payment_option = st.radio(
                '',
                (Text.none_selected, Text.radio_pay_fixed_rate, Text.radio_pay_adjusted_rate)
            )
            step_four_submit = st.form_submit_button(Text.line)
            if step_four_submit:
                is_step_four.checkboxed = True

        return payment_option


def convert_to_isk(amount):
    return locale.currency(amount, grouping=True)


# Part of Step 3
def calculate_non_indexed(principal, interest, duration):
    isk = locale.currency(int(principal), grouping=True)
    _interest = float(interest)
    _duration = int(duration)

    st.markdown(Text.step_3)
    st.markdown(f'### {Text.loan_amount}: {isk}')
    st.markdown(f'### {Text.duration}: {_duration}')
    st.markdown(f'### {Text.interest_rate}: {_interest}%')
    st.markdown(f'*{Text.if_wrong_input}*')

    nil = NonIndexedLinked(int(principal), _duration, _interest)
    nil.non_index_calculation()

    st.markdown(f'### {Text.monthly_payments}: {convert_to_isk(nil.total_payment_list[0])}')
    st.markdown(f'### {Text.total_loan_payment}: {convert_to_isk(sum(nil.total_payment_list))}')
    st.markdown(f'### {Text.total_interest_payment}: {convert_to_isk(sum(nil.interest_list))}')


def calculate_indexed(principal, interest, duration, inflation):
    isk = locale.currency(int(principal), grouping=True)
    _interest = float(interest)
    _duration = int(duration)
    _inflation = float(inflation)

    st.markdown(Text.step_3)
    st.markdown(f'### {Text.loan_amount}: {isk}')
    st.markdown(f'### {Text.duration}: {_duration}')
    st.markdown(f'### {Text.interest_rate}: {_interest}%')
    st.markdown(f'*{Text.if_wrong_input}*')

    il = IndexLinked(int(principal), _duration, _interest, _inflation)
    il.index_calculation()

    st.markdown(f'### {Text.monthly_payments}: {convert_to_isk(il.total_payment_list[0])}')
    st.markdown(f'### {Text.total_loan_payment}: {convert_to_isk(sum(il.total_payment_list))}')
    st.markdown(f'### {Text.total_interest_payment}: {convert_to_isk(sum(il.interest_list))}')

    st.markdown(f'{Text.stop_getting_ripped_off}')


if __name__ == '__main__':
    # Used to keep track of the states
    is_step_one = SessionState.get(checkboxed=False)
    is_step_two = SessionState.get(checkboxed=False)
    is_step_three = SessionState.get(checkboxed=False)
    is_step_four = SessionState.get(checkboxed=False)

    # The layout of the website
    # Header and introduction text for the website
    st.markdown(Text.header)
    st.markdown(Text.line)
    st.markdown(Text.intro_text)

    loan_type = step_one()
    principal, interest, duration, inflation, is_indexed = step_two(loan_type)
    step_three(principal, interest, duration, inflation, is_indexed)
    step_four()
