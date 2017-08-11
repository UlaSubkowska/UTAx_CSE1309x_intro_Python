def remaining_balance(principal, annual_interest_rate, duration,number_of_payments ):
    monthly_interest_rate=(annual_interest_rate/100)/12
    r=monthly_interest_rate
    total_of_monthly_payments=duration*12
    n=total_of_monthly_payments
    p=number_of_payments
    if r!=0:
        remaining_loan=principal*(((1+r)**n-(1+r)**p)/((1+r)**n-1))
    else:
        remaining_loan=principal*(1-p/n)
    return remaining_loan