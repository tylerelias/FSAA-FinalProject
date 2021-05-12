import streamlit as st
from text.text import Text


def loan_text_input():
    st.text_input(Text.loan_amount, "0")
    st.text_input(Text.interest_rate, "0.0")
    st.text_input(Text.duration, "0")


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
    loan_text_input()
    if st.button(Text.done):
        st.write("Smellt")

# Second step - indexed
if loan_type == Text.indexed:
    st.markdown(Text.line)
    st.markdown(Text.selected_indexed)
    st.markdown(Text.step_2)
    loan_text_input()
    st.text_input(Text.inflation_rate, "0.0")
    if st.button(Text.done):
        st.write("Smellt")