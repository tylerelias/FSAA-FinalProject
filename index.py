import streamlit as st
from calculations.indexed import IndexLinked
from calculations.nonindexed import NonIndexedLinked

import locale
import SessionState
from text.text import Text

locale.setlocale(locale.LC_ALL, 'is_IS.UTF-8')


@st.cache(allow_output_mutation=True)
def button_states():
    return {"pressed": None}


def step_one():
    # The checkbox where the user selects the type of loan to fill out
    st.markdown(Text.step_1)
    loan_type = st.radio(
        '',
        (Text.none_selected, Text.non_indexed, Text.indexed),
        key='step_one'
    )

    step_two(loan_type)


def step_two(loan_type):
    # non-indexed loans
    if loan_type == Text.non_indexed:
        with st.form("non_indexed"):
            st.markdown(Text.selected_non_indexed)
            st.markdown(Text.step_2)

            principal, interest, duration = loan_text_input()

            submit = st.form_submit_button(Text.submit)
            is_step_two = button_states()
            if submit:
                # TODO: Input validation !!!
                is_step_two.update({"pressed": True})

        step_three(principal, interest, duration, is_step_two, is_indexed=True)

    # Second step - indexed
    if loan_type == Text.indexed:
        with st.form("indexed"):
            st.markdown(Text.selected_indexed)
            st.markdown(Text.step_2)

            principal, interest, duration = loan_text_input()
            inflation = st.text_input(
                Text.inflation_rate,
                "4.6",
                help=Text.inflation_rate_help
            )

            submit = st.form_submit_button(Text.submit)
            is_step_two = button_states()
            if submit:
                # TODO: Input validation !!!
                is_step_two.update({"pressed": True})

        step_three(principal, interest, duration, is_step_two, False, inflation)


def step_three(principal, interest, duration, is_step_two, is_indexed, inflation=0.0):
    if is_step_two["pressed"] and is_indexed is False:
        with st.form("non_indexed_overview"):

            calculate_non_indexed(principal, interest, duration)
            step_three_submit = st.form_submit_button(Text.btn_step4)
            is_step_three = button_states()
            if step_three_submit:
                is_step_three.update({"pressed": True})
        step_four(is_step_three)

    if is_step_two["pressed"] and is_indexed is True:
        with st.form("indexed_overview"):

            calculate_indexed(principal, interest, duration, inflation)
            step_three_submit = st.form_submit_button(Text.btn_step4)
            is_step_three = button_states()
            if step_three_submit:
                is_step_three.update({"pressed": True})
        step_four(is_step_three)


def step_four(is_step_three):
    with st.form("step_four"):
        if is_step_three["pressed"]:
            st.markdown(Text.step_4)
            payment_option = st.radio(
                '',
                (Text.none_selected, Text.radio_pay_fixed_rate, Text.radio_pay_adjusted_rate)
            )
            step_four_submit = st.form_submit_button(Text.btn_step4)
            is_step_four = button_states()
            if step_four_submit:
                is_step_four.update({"pressed": True})

        return payment_option


def convert_to_isk(amount):
    return locale.currency(amount, grouping=True)


def loan_text_input():
    amount = st.text_input(
        Text.loan_amount,
        "0",
        help=Text.amount_help
    )
    duration = st.text_input(
        Text.duration,
        "0",
        help=Text.duration_help
    )
    interest = st.text_input(
        Text.interest_rate,
        "0.0",
        help=Text.interest_rate_help
    )

    return amount, interest, duration


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


# The layout of the website
session = SessionState.get(run_id=0)
if st.button(Text.reset):
    st.caching.clear_cache()
    session.run_id += 1

# Header and introduction text for the website
st.markdown(Text.header)
st.markdown(Text.line)
st.markdown(Text.intro_text)

step_one()

