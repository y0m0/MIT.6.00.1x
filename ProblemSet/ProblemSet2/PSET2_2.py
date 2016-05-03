balance = 3926
annualInterestRate = 0.2
minimumpayment = 10


def notpaid(b,i,m):
    count = 0
    while count < 12:
        u = round((b-m),2)
        b = round((u + (i/12.0) * u),2)
        count += 1
    return b


while notpaid(balance,annualInterestRate,minimumpayment) > 0.0:
    minimumpayment += 10

print 'Lowest Payment:', minimumpayment
