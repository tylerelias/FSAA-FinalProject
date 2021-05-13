import locale
import streamlit as st
import SessionState
from calculations.indexed import IndexLinked
from calculations.nonindexed import NonIndexedLinked
from text.text import Text
locale.setlocale(locale.LC_ALL, 'is_IS.UTF-8')

# Used to keep track of the states
ss = SessionState.get(
    one=False,
    two=False,
    three=False,
    four=False,
    principal='0',
    duration='0',
    interest='0.0',
    inflation='0.0',
    is_indexed=False
)

def loan_text_input():
    ss.principal = st.text_input(
        Text.loan_amount,
        '0' if ss.principal == '0' else ss.principal,
        help=Text.amount_help
    )
    ss.duration = st.text_input(
        Text.duration,
        '0' if ss.duration == '0' else ss.duration,
        help=Text.duration_help
    )
    ss.interest = st.text_input(
        Text.interest_rate,
        '0.0' if ss.interest == '0.0' else ss.interest,
        help=Text.interest_rate_help
    )

    return ss.principal, ss.duration, ss.interest


def validate_input():
    if not ss.principal.isnumeric() or int(ss.principal) < 1:
        return False
    if not ss.duration.isnumeric() or int(ss.duration) < 1:
        return False
    if not ss.interest.replace('.', '', 1).isdigit() or float(ss.interest) < 0:
        return False
    if not ss.inflation.replace('.', '', 1).isdigit():
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

def no_missing_parameters(loan_type):
    if(loan_type == 'non_indexed'):
        return ss.principal != '0' and ss.duration != '0' and ss.interest != '0.0'
    elif(loan_type == 'indexed'):
        return ss.principal != '0' and ss.duration != '0' and ss.interest != '0.0' and ss.inflation != '0.0'

def step_two_form(loan_type = '', markdown_text=''):
    st.markdown(markdown_text)
    st.markdown(Text.step_2)
    # Print out the various stats
    ss.principal, ss.duration, ss.interest = loan_text_input()
    ss.is_indexed = False

    if loan_type == "indexed":
        ss.inflation = st.text_input(
            Text.inflation_rate,
            '0.0' if ss.inflation == '0.0' else ss.inflation,
            help=Text.inflation_rate_help
        )
        ss.is_indexed = True

    if no_missing_parameters(loan_type):
        input_validation = validate_input()
        if input_validation:
            ss.two = True
        else:
            # TODO: Fix to make a proper Wrong Value message
            ss.two = False
            st.markdown("## Illegal input")
        
def step_two(loan_type):

    # non-indexed loans
    if loan_type == Text.non_indexed:
        # The form
        #with st.form("non_indexed"):
        step_two_form("non_indexed", Text.selected_non_indexed)

    # Second step - indexed
    if loan_type == Text.indexed:

        #with st.form("indexed"):
        step_two_form("indexed", Text.selected_indexed)

    #return ss.principal, ss.interest, ss.duration, ss.inflation, ss.is_indexed

def step_three():
    # For non-indexed case
    if ss.two and ss.is_indexed is False:
        with st.form("non_indexed_overview"):
            calculate_non_indexed()
            step_three_submit = st.form_submit_button(Text.btn_step4)
            # st.write(is_step_three.three)
            if step_three_submit:
                ss.three = True

    # For indexed loan case
    if ss.two and ss.is_indexed is True:
        with st.form("indexed_overview"):
            calculate_indexed()
            step_three_submit = st.form_submit_button(Text.btn_step4)
            if step_three_submit:
                ss.three = True


def step_four():
    # st.write(is_step_three.checkboxed)
    if ss.three:
        with st.form("step_four"):
            st.markdown(Text.step_4)
            payment_option = st.radio(
                '',
                (Text.none_selected, Text.radio_pay_fixed_rate, Text.radio_pay_adjusted_rate)
            )
            step_four_submit = st.form_submit_button(Text.line)
            if step_four_submit:
                ss.four = True

        return payment_option


def convert_to_isk(amount):
    return locale.currency(amount, grouping=True)


# Part of Step 3
def display_info(loan_type):
    isk = locale.currency(int(ss.principal), grouping=True)
    _interest = float(ss.interest)
    _duration = int(ss.duration)

    st.markdown(Text.step_3)
    st.markdown(f'### {Text.loan_amount}: {isk}')
    st.markdown(f'### {Text.duration}: {_duration}')
    st.markdown(f'### {Text.interest_rate}: {_interest}%')
    st.markdown(f'*{Text.if_wrong_input}*')

    if(loan_type == "indexed"):
        _inflation = float(ss.inflation)
        lt = IndexLinked(int(ss.principal), _duration, _interest, _inflation)
        lt.index_calculation()
    elif(loan_type == "non_indexed"):
        lt = NonIndexedLinked(int(ss.principal), _duration, _interest)
        lt.non_index_calculation()

    st.markdown(
        f'### {Text.monthly_payments}: {convert_to_isk(lt.total_payment_list[0])}')
    st.markdown(
        f'### {Text.total_loan_payment}: {convert_to_isk(sum(lt.total_payment_list))}')
    st.markdown(
        f'### {Text.total_interest_payment}: {convert_to_isk(sum(lt.interest_list))}')

    #if(tegund == "indexed"):
    #st.markdown(f'{Text.stop_getting_ripped_off}')


def calculate_non_indexed():
    display_info("non_indexed")


def calculate_indexed():
    display_info("indexed")


if __name__ == '__main__':


    # The layout of the website
    # Header and introduction text for the website
    st.markdown(Text.header)
    st.markdown(Text.line)
    st.markdown(Text.intro_text)

    loan_type = step_one()
    #ss.principal, ss.interest, ss.duration, ss.inflation, ss.is_indexed = step_two(loan_type)
    step_two(loan_type)
    step_three()
    step_four()
