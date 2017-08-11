from monthly_payments import *
from remaining_balance_of_a_loan import *

principal = int(input('Type the total amount of loan:'))
annual_interest_rate = float(input('Type the annual interest rate per year (percent without % sign):'))
duration = int(input('Type the total duration of loan in years: '))

monthly_payment = monthly_payments(principal, annual_interest_rate, duration)

print('LOAN AMOUNT:', principal, 'INTEREST RATE (PERCENT):', annual_interest_rate)
print('DURATION (YEARS):', duration, 'MONTHLY PAYMENT:', int(monthly_payment))

year = 1
while year <= duration:
    balance = remaining_balance(principal, annual_interest_rate, duration, year * 12)
    total_payment = monthly_payment * 12 * year
    print('YEAR:', year, 'BALANCE:', int(balance), 'TOTAL PAYMENT:', int(total_payment))
    year += 1