"""
Name: Derek Bolch
interest.py

Problem: this program will help the user determine their credit card interest

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():

    # Taking in the required user inputs
    annual_interest = eval(input("Enter the annual interest rate: "))
    billing_cycle_length = eval(input("Enter the amount of days in the billing cycle: "))
    net_balance = eval(input("Enter the previous net balance: "))
    payment_amount = eval(input("Enter the amount paid: "))
    day_paid = eval(input("Enter the day of the billing cycle in which the payment was made: "))

    # STEP ONE: Multiplies net balance by billing cycle length
    x_1 = net_balance * billing_cycle_length

    # STEP TWO: Determines days remaining in billing cycle
    # and multiplies that by net payment received
    days_remaining = billing_cycle_length - day_paid
    x_2 = payment_amount * days_remaining

    # STEP THREE: Subtracts the result of step one by the results of step two
    x_3 = x_1 - x_2

    # STEP FOUR: Takes results of step three and divides by the length of the billing cycle
    avg_daily_balance = x_3 / billing_cycle_length

    # STEP FIVE: Converts annual interest rate into monthly interest rate
    # and change percentage to decimal number
    monthly_interest = annual_interest / 12
    decimal_interest = monthly_interest / 100

    # STEP SIX: Calculates final monthly interest charge and prints result
    monthly_interest_charge = avg_daily_balance * decimal_interest
    print(round(monthly_interest_charge, 2))


if __name__ == '__main__':
    main()
