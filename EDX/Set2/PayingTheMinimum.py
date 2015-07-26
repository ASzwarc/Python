__author__ = 'aszwarc'

# balance = 4213
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
minimumPayment = 0.0
unpaidBalance = 0.0
interest = 0.0
total = 0.0
for month in range(1, 13):
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = annualInterestRate / 12.0 * unpaidBalance
    balance = unpaidBalance + interest
    if month > 0:
        total += minimumPayment
        print "Month: " + str(month)
        print("Minimum monthly payment: %.2f" % minimumPayment)
        print ("Remaining balance: %.2f" % balance)
print("Total paid: %.2f" % total)
print ("Remaining balance: %.2f" % balance)