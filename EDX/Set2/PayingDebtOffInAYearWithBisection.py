__author__ = 'aszwarc'

balance = 999999
annualInterestRate = 0.18
balanceToCalculate = balance
epsilon = 0.01
monthlyPaymentLowerBound = balance / 12.0
monthlyPaymentUpperBound = (balance * (1 + annualInterestRate / 12.0) ** 12) / 12.0
while True:
    balanceToCalculate = balance
    minimumPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2.0
    print "Lower bound : " + str(monthlyPaymentLowerBound)
    print "Upper bound : " + str(monthlyPaymentUpperBound)
    print "Minimum payment : " + str(minimumPayment)
    for month in range(1, 13):
        unpaidBalance = balanceToCalculate - minimumPayment
        interest = annualInterestRate / 12.0 * unpaidBalance
        balanceToCalculate = unpaidBalance + interest

    print "Balance at end of the year : " + str(balanceToCalculate)
    if abs(balanceToCalculate) < epsilon:
        print "Lowest Payment: %.2f" % minimumPayment
        break
    else:
        if balanceToCalculate > 0:
            monthlyPaymentLowerBound = minimumPayment
        elif balanceToCalculate < 0:
            monthlyPaymentUpperBound = minimumPayment