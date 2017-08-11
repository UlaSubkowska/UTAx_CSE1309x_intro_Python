def monthly_payments(principal, annual_interest_rate, duration):
    monthly_interest_rate=(annual_interest_rate/100)/12
    r=monthly_interest_rate
    total_of_monthly_payments=duration*12
    n=total_of_monthly_payments
    if r!=0:
        monthly_payment=principal*((r*(1+r)**n)/((1+r)**n-1))
    else:
        monthly_payment=principal/n
    return monthly_payment
