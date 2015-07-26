__author__ = 'aszwarc'

balance = 3926
annualInterestRate = 0.2
minimumPayment = 10
stopLoop = False
balanceToCalculate = balance
while not stopLoop:
    for month in range(1, 13):
        unpaidBalance = balanceToCalculate - minimumPayment
        interest = annualInterestRate / 12.0 * unpaidBalance
        balanceToCalculate = unpaidBalance + interest

    if balanceToCalculate <= 0:
        stopLoop = True
        print "Lowest Payment: " + str(minimumPayment)
    else:
        minimumPayment += 10
        balanceToCalculate = balance
