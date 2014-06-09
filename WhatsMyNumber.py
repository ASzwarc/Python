__author__ = 'Adam'
from math import sqrt

def erastothenesSieve(maxNumber):
    """Program that returns list of prime numbers from 1 to maxNumber"""
    maxNumber += 1
    primes = range(1, maxNumber)
    for n in range(2, int(sqrt(maxNumber) + 1)) :
        for number in primes :
            if ((number % n == 0) and (number != n)) :
                primes.remove(number)
    #print "Returning list : ", primes
    return primes
def numberHasTwoDigits(primeNumbers):
    result = []
    for element in primeNumbers :
        if ( int(element / 10) != 0) :
            result.append(element)
    #print "list was changed to : ", result
    return result
def decomposeNumberToSingleDigit(number):
    digits = []
    for element in str(number) :
        digits.append(int(element))
    return digits
def checkIfNumberHas1Or7(elementList):
    result = []
    for element in elementList :
        has1Or7 = False
        for digit in decomposeNumberToSingleDigit(element) :
            if (digit == 1 or digit == 7) :
                has1Or7 = True
                break
        if (has1Or7 == False) :
            result.append(element)
    return result
def sumIsLessOrEqual10(elementList) :
    result = []
    for element in elementList :
        sum = 0
        for digit in decomposeNumberToSingleDigit(element) :
            sum += digit
        if (sum <= 10) :
            result.append(element)
    return result
def firstTwoDigitsAreOdd(elementList) :
    result = []
    for element in elementList :
        if ((decomposeNumberToSingleDigit(element)[0] + decomposeNumberToSingleDigit(element)[1]) % 2 != 0) :
            result.append(element)
    return result
def secondToLastDigitIsOdd(elementList) :
    result = []
    for element in elementList :
        digitsOfNumber = decomposeNumberToSingleDigit(element)
        if(digitsOfNumber[-2] % 2 == 0) :
            result.append(element)
    return result

def lastDigitIsEqualToNumberOfDigits(elementList) :
    result = []
    for element in elementList :
        digitsOfNumber = decomposeNumberToSingleDigit(element)
        if (digitsOfNumber[-1] == len(digitsOfNumber)) :
            result.append(element)
    return result
print "Im checking if prime numbers generator works"
results = erastothenesSieve(1000)
numberWithTwoDigits = numberHasTwoDigits(results)
numbersWithout1Or7 = checkIfNumberHas1Or7(numberWithTwoDigits)
numberWithSumLessOrEqual10 = sumIsLessOrEqual10(numbersWithout1Or7)
numberWithOddFirstTwoDigits = firstTwoDigitsAreOdd(numberWithSumLessOrEqual10)
numberWithSecondToLastDigitOdd = secondToLastDigitIsOdd(numberWithOddFirstTwoDigits)
theNumber = lastDigitIsEqualToNumberOfDigits(numberWithSecondToLastDigitOdd)

print "Output : ", theNumber
