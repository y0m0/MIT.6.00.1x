balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


month = 1
totalpaid = 0
for i in range(0,12):
    minimumpayment = round((balance*monthlyPaymentRate),2)
    unpaidBalance = round((balance-minimumpayment),2)
    balance = round((unpaidBalance + (annualInterestRate/12.0) * unpaidBalance),2)
    totalpaid += minimumpayment

    print 'Month:', month
    print 'Minimum monthly payment:', minimumpayment
    print 'Remaining balance:', balance
    month += 1
print 'Total Paid:', totalpaid
print 'Remaining Balance:', balance
