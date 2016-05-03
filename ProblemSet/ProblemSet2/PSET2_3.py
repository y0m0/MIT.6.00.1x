balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
lowerPayment = balance/12.0
minimumPayment = lowerPayment
highestPayment = (balance*(1 + monthlyInterestRate)**12)/12

#Calcola bilancio dopo 12mesi dato un pagamento minimo m


def notpaid(b, a, m):

    for x in range(12):
        u = round((b-m), 2)
        b = round((u + (a/12.0) * u), 2)
    return b


#Soluzione 2


def guess(l, h, m, n):
    while x is True:
        if n > 0.01:
            l = m
            m = (l + h)/2
            return m
        elif n < - 0.01:
            h = m
            m = (l + h)/2
            return m
        else:
            x = False
            return m
    return m



print 'Lowest Payment:', guess(lowerPayment, highestPayment, minimumPayment, notpaid(balance, annualInterestRate,
                                                                                     minimumPayment))

#Soluzione 1

# while True:
#     if notpaid(balance, annualInterestRate, minimumPayment) > 0.1:
#         lowerPayment = minimumPayment
#         minimumPayment = (lowerPayment + highestPayment)/2
#
#     elif notpaid(balance, annualInterestRate, minimumPayment) < - 0.1:
#         highestPayment = minimumPayment
#         minimumPayment = (lowerPayment + highestPayment)/2
#
#     else:
#         print 'Lowest Payment:', round(minimumPayment, 2)
#         break
