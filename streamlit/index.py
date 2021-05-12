import streamlit as st
from text.text import Text


def loan_text_input():
    amount = st.text_input(
        Text.loan_amount,
        "0",
        help=Text.amount_help
    )
    interest = st.text_input(
        Text.interest_rate,
        "0.0",
        help=Text.interest_rate_help
    )
    duration = st.text_input(
        Text.duration,
        "0",
        help=Text.duration_help
    )

    return amount, interest, duration


def calculate_non_indexed(amount, interest, duration):
    st.write(amount, interest, duration)


def calculate_indexed(amount, interest, duration, inflation):
    st.write(amount, interest, duration, inflation)


# The layout of the website

# Header and introduction text for the website
st.markdown(Text.header)
st.markdown(Text.line)
st.markdown(Text.intro_text)

# The first step
st.markdown(Text.step_1)
loan_type = st.radio(
    '',
    (Text.none_selected, Text.non_indexed, Text.indexed)
)

# Second step - non indexed

if loan_type == Text.non_indexed:
    st.markdown(Text.line)
    st.markdown(Text.selected_non_indexed)
    st.markdown(Text.step_2)

    amount, interest, duration = loan_text_input()

    if st.button(Text.done):
        st.markdown(Text.line)
        calculate_non_indexed(amount, interest, duration)

# Second step - indexed
if loan_type == Text.indexed:
    st.markdown(Text.line)
    st.markdown(Text.selected_indexed)
    st.markdown(Text.step_2)

    amount, interest, duration = loan_text_input()
    inflation = st.text_input(
        Text.inflation_rate,
        "4.6",
        help=Text.inflation_rate_help
    )

    if st.button(Text.done):
        st.markdown(Text.line)
        calculate_indexed(amount, interest, duration, inflation)
