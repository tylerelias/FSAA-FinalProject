import locale
import pandas as pd
import streamlit as st
from PIL import Image
from calculations.indexed import IndexLinked
from calculations.nonindexed import NonIndexedLinked
from text.text import Text

# Current inflation, look into making this value auto-updating
INFLATION = 4.6
# Sets the currency to ISK
locale.setlocale(locale.LC_ALL, "is_IS.UTF-8")

# Used to keep track of the states
one = False  # Not needed?
two = False
three = False
four = False
principal = 0
duration = 0
interest = 0.0
inflation = 0.0
is_indexed = False
extra_payment = 5000
principal_list = []
payed_interest = []
monthly_payments = []
total_loan_amount = 0
saved = []
cost = 0
total_loan_payment = 0.0

def convert_to_isk(amount):
    return locale.currency(amount, grouping=True)


def make_same_size():
    global principal_list
    global saved

    len_principal = len(principal_list)
    len_saved = len(saved)

    # have to make principal and saved be the same size to plot
    tmp_saved = saved
    if len_saved < len_principal:
        for i in range(len_principal - len_saved):
            tmp_saved.append(0)
    return tmp_saved


def show_loan_saved_graph():
    global principal_list
    global saved

    st.write(f"# {Text.graph_title}")
    # we don't wanna update the actual saved array so we create a local variable
    saved = make_same_size()

    if saved != 0:
        df = pd.DataFrame(
            {Text.without_payments: principal_list, Text.with_payments: saved}
        )
    st.line_chart(df)


# Part of Step 3
def display_info(loan_type):
    global principal_list
    global payed_interest
    global monthly_payments
    global total_loan_amount
    global total_loan_payment
    # loan amount in icelandic krona
    isk = locale.currency(principal, grouping=True)
    # year month left
    year_left, month_left = format_time_saved(duration)

    st.markdown(Text.step_3)
    st.markdown(f"#### {Text.loan_amount}: {isk}")
    # st.markdown(f"### {Text.duration}: {duration}")

    if month_left > 0:
        st.markdown(
            f"#### {Text.loan_duration}: {year_left} {Text.years_and} {month_left} {Text.months} "
        )
    elif month_left <= 0:
        st.markdown(f"#### {Text.loan_duration}: {year_left} {Text.years}")

    st.markdown(f"#### {Text.interest_rate}: {interest}%")

    other_loan_type = ""
    lt_indexation = 0
    ot_indexation = 0
    if loan_type == Text.indexed:
        st.markdown(f"#### {Text.inflation_rate}: {inflation}%")
        # calculate the chosen loan
        lt = IndexLinked(principal, duration, interest, inflation, cost=cost)
        lt.index_calculation()
        # calculated the other loan to compare results
        other_loan_type = Text.non_indexed
        ot = NonIndexedLinked(principal, duration, interest + 1.5, cost=cost)
        ot.non_index_calculation()
        # Indexation calculation and display
        lt_indexation = lt.get_total_indexation()

    elif loan_type == Text.non_indexed:
        # calculate the chosen loan
        lt = NonIndexedLinked(principal, duration, interest, cost=cost)
        lt.non_index_calculation()
        # calculated the other loan to compare results
        other_loan_type = Text.indexed
        ot = IndexLinked(principal, duration, interest - 1.5, INFLATION, cost=cost)
        ot.index_calculation()
        ot_indexation = ot.get_total_indexation()

    st.markdown(Text.linebreak)
    with st.beta_expander(Text.wrong_input):
        st.markdown(f"{Text.if_wrong_input}")

    avg_monthly_payment = sum(lt.total_payment_list) / len(lt.total_payment_list)
    interest_list_sum = sum(lt.interest_list)
    total_amount_paid = interest_list_sum + principal

    # Monthly payment section
    lt_avg_m_payments = convert_to_isk(avg_monthly_payment)
    lt_first_monthly_payment = convert_to_isk(lt.total_payment_list[0])
    lt_last_monthly_payment = convert_to_isk(lt.total_payment_list[-1])

    st.markdown(f"## {Text.monthly_payments_title}")
    st.markdown(f"{Text.monthly_payments_desc}")

    st.markdown(f"### {Text.avg_monthly_payments}: {lt_avg_m_payments}")
    # Give more info if the loan is indexed, highlight how truly awful they end up being
    if loan_type == Text.indexed:
        st.markdown(f"### {Text.first_monthly_payments}: {(lt_first_monthly_payment)}")
        st.markdown(f"### {Text.last_monthly_payments}: {(lt_last_monthly_payment)}")
    st.markdown(Text.linebreak)
    with st.beta_expander(Text.monthly_payments_info):
        st.markdown(f"{Text.monthly_payments_info_desc}")

    # Chart to compare monthly payments
    df = pd.DataFrame(
        {loan_type: lt.total_payment_list, other_loan_type: ot.total_payment_list}
    )
    st.markdown(f"# {Text.payment_chart}")
    st.markdown(f"{Text.payment_chart_desc}")
    st.line_chart(df)
    st.markdown(Text.linebreak)

    # Payed interest section
    st.markdown(f"## {Text.interest_title}")
    st.markdown(f"{Text.interest_desc}")
    # Total interest payments
    lt_total_interest_payment = convert_to_isk(sum(lt.interest_list))
    st.markdown(f"### {Text.total_interest_payment}: {lt_total_interest_payment}")
    st.markdown(Text.linebreak)
    with st.beta_expander(Text.total_interest_payment_help):
        st.markdown(f"{Text.total_interest_payment_desc}")
    # Total loan payment

    # Indexations
    lt_indexation = convert_to_isk(lt_indexation)
    ot_indexation = convert_to_isk(ot_indexation)

    st.markdown(f"## {Text.indexation}")
    st.markdown(f"{Text.indexation_desc}")
    st.markdown(f"### {Text.payed_indexation}: {lt_indexation}")
    st.markdown(Text.linebreak)
    with st.beta_expander(Text.indexation_help):
        st.markdown(f"{Text.indexation_info}")

    lt_total_loan_payment = convert_to_isk(lt.get_total_payment())

    st.markdown(f"## {Text.total_loan_payment}")
    st.markdown(f"{Text.total_loan_payment_info}")
    st.markdown(f"### {Text.total_loan_payment}: {lt_total_loan_payment}")
    st.markdown(Text.linebreak)
    with st.beta_expander(Text.total_loan_payment_help):
        st.markdown(f"{Text.total_loan_payment_desc}")
    # Compare with other_loan
    ot_total_loan_payment = convert_to_isk(ot.get_total_payment())
    other_loan_tolower = str(other_loan_type).lower()
    ot_total_interest_payment = convert_to_isk(sum(ot.interest_list))
    ot_avg_m_payments = convert_to_isk(
        sum(ot.total_payment_list) / len(ot.total_payment_list)
    )
    ot_first_monthly_payment = convert_to_isk(ot.total_payment_list[0])
    ot_last_monthly_payment = convert_to_isk(ot.total_payment_list[-1])
    total_loan_amount = convert_to_isk(principal)
    lt_cost = convert_to_isk(lt.cost * lt.duration)
    ot_cost = convert_to_isk(ot.cost * ot.duration)

    st.markdown(f"## {Text.compare_loans_title}")
    st.markdown(
        f"{Text.compare_loans_desc_pt1} {other_loan_tolower} {Text.compare_loans_desc_pt2}"
    )
    st.markdown(
        f"""
| {Text.section}                | {loan_type}                 | {other_loan_type}           |
|-------------------------------|-----------------------------|-----------------------------|
| {Text.loan_amount}            | {total_loan_amount}         | {total_loan_amount}         |
| {Text.indexation}             | {lt_indexation}             | {ot_indexation}             |
| {Text.total_interest_payment} | {lt_total_interest_payment} | {ot_total_interest_payment} |
| {Text.cost}                   | {lt_cost}                   | {ot_cost}                   |
| {Text.total_loan_payment}     | **{lt_total_loan_payment}** | **{ot_total_loan_payment}** |
| **{Text.monthy_payments}**    |                             |                             |
| {Text.first_monthly_payments} | {lt_first_monthly_payment}  | {ot_first_monthly_payment}  |
| {Text.avg_monthly_payments}   | {lt_avg_m_payments}         | {ot_avg_m_payments}         |
| {Text.last_monthly_payments}  | {lt_last_monthly_payment}   | {ot_last_monthly_payment}   |
    """
    )

    st.markdown(Text.linebreak)
    st.markdown(Text.linebreak)
    with st.beta_expander(Text.compare_loans_help):
        st.markdown(f"{Text.compare_loans_info}")

    principal_list = lt.principal_list
    payed_interest = lt.interest_list
    monthly_payments = avg_monthly_payment
    total_loan_amount = total_amount_paid
    total_loan_payment = lt.get_total_payment()


def calculate_non_indexed():
    display_info(Text.non_indexed)


def calculate_indexed():
    display_info(Text.indexed)


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
    if loan_type == Text.non_indexed:
        return principal != 0 and duration != 0 and interest != 0.0 and cost != 0
    elif loan_type == Text.indexed:
        return (
                principal != 0
                and duration != 0
                and interest != 0.0
                and inflation != 0.0
                and inflation != 0
                and cost != 0
        )


if __name__ == "__main__":
    # The layout of the website
    # Header and introduction text for the website
    st.markdown(f"# {Text.header}")
    st.markdown(Text.line)
    st.markdown(Text.intro_text)

    # The checkbox where the user selects the type of loan to fill out
    st.markdown(Text.step_1)
    loan_type = st.radio(
        "", (Text.none_selected, Text.non_indexed, Text.indexed), key="step_one"
    )
    with st.beta_expander(Text.n_idx_diff):
        img_non_idx = Image.open("img/non_indexed.png")
        img_idx = Image.open("img/indexed.png")
        img_idx_exp = Image.open("img/indexed_more_exp.png")
        # Detailed explanation
        st.markdown(Text.index_vs_nonindex)
        # images with desc
        st.markdown(f"### {Text.img_idx_title}")
        st.image(img_idx, caption=Text.img_idx_desc)

        st.markdown(f"### {Text.img_non_idx_title}")
        st.image(img_non_idx, caption=Text.img_non_idx_desc)

        st.markdown(f"### {Text.img_idx_exp_title}")
        st.image(img_idx_exp, caption=Text.img_idx_exp_desc)

    if loan_type == Text.none_selected:
        two = False
        three = False
        four = False

    # Step 2
    if loan_type != Text.none_selected:
        if loan_type == Text.non_indexed:
            is_indexed = False
        else:
            is_indexed = True
        # The form

        # Text for the site
        if loan_type == Text.non_indexed:
            st.markdown(Text.selected_non_indexed)
            st.markdown(Text.selected_non_indexed_info)
        elif loan_type == Text.indexed:
            st.markdown(Text.selected_indexed)
            st.markdown(Text.selected_indexed_info)

        st.markdown(Text.line)
        st.markdown(Text.step_2)

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

        if no_missing_parameters(loan_type):
            two = True

    # Step 3
    st.markdown(Text.line)
    # For non-indexed case
    if two and is_indexed is False:
        calculate_non_indexed()
        three = True

    # For indexed loan case
    if two and is_indexed is True:
        calculate_indexed()
        three = True

    # Step 4
    if three:
        st.markdown(Text.line)
        st.markdown(Text.step_4)
        st.markdown(Text.pay_adjusted_rate)

        with st.beta_expander(Text.adj_fix_difference):
            st.markdown(Text.pay_adjusted_rate_example)

        extra_payment = st.number_input(
            Text.extra_payment,
            value=extra_payment,
            help=Text.extra_payment_help,
            min_value=1000,
            max_value=1000000,
            step=5000,
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
                st.markdown(
                    f"### {Text.monthly_extra_payment1} {convert_to_isk(extra_payment)} {Text.monthly_extra_payment2}"
                )
                st.markdown(f"### {Text.money_saved}: {convert_to_isk(money_saved)}")
                st.markdown(
                    f"### {Text.time_saved}: {year} {Text.years_and} {month} {Text.months} "
                )
                st.markdown(f"###")
                st.markdown(
                    f"### {Text.total_loan}: {convert_to_isk(total_loan_amount - money_saved)}"
                )
                if month_left_now > 0:
                    st.markdown(
                        f"### {Text.loan_shortened_now} {year_left_now} {Text.years_and} {month_left_now} {Text.months} "
                    )

                elif month_left_now <= 0:
                    st.markdown(
                        f"### {Text.loan_shortened_now} {year_left_now} {Text.years}"
                    )
                saved = nil.principal_list
                show_loan_saved_graph()

        elif is_indexed:
            # Doesn't really matter how much you try to pay into the loan,
            # the capital will keep growing by hundreds of thousands, make this case to
            # the person using the calculator and suggest a refinance on their current loan
            il = IndexLinked(principal, duration, interest, inflation, cost=cost)
            money_saved = il.total_saved_from_extra_payment(extra_payment)
            year, month = format_time_saved(
                il.time_saved_from_extra_payment(extra_payment)
            )
            # year month left
            months_shortened = duration - (year * 12 + month)
            year_left_now, month_left_now = format_time_saved(months_shortened)

            if extra_payment > 0:
                st.markdown(
                    f"### {Text.monthly_extra_payment1} {convert_to_isk(extra_payment)} {Text.monthly_extra_payment2}"
                )
                st.markdown(f"### {Text.money_saved}: {convert_to_isk(money_saved)}")
                st.markdown(
                    f"### {Text.time_saved}: {year} {Text.years_and} {month} {Text.months} "
                )
                st.markdown(f"###")
                st.markdown(
                    f"### {Text.total_loan}: {convert_to_isk(total_loan_payment - money_saved)}"
                )
                if month_left_now > 0:
                    st.markdown(
                        f"### {Text.loan_shortened_now} {year_left_now} {Text.years_and} {month_left_now} {Text.months} "
                    )

                elif month_left_now <= 0:
                    st.markdown(
                        f"### {Text.loan_shortened_now} {year_left_now} {Text.years}"
                    )
                saved = il.principal_list
                show_loan_saved_graph()
