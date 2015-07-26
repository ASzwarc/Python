__author__ = 'aszwarc'
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif exp > 0 and exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    elif exp > 0 and exp % 2 != 0:
        return base * recurPowerNew(base, exp - 1)

print recurPowerNew(4, 3)

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test_value = a if a <= b else b
    while test_value > 1:
        if a % test_value == 0 and b % test_value == 0:
            return test_value
        else:
            test_value -= 1
    return 1

print "gcdIter : "
print gcdIter(1, 2)
print gcdIter(2, 2)
print gcdIter(12, 17)
print gcdIter(6, 12)
print gcdIter(1, 1)

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print "gcdRecur"
print gcdRecur(1, 2)
print gcdRecur(2, 2)
print gcdRecur(12, 17)
print gcdRecur(6, 12)
print gcdRecur(1, 1)

def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    retVal = 0
    for char in aStr:
        retVal += 1
    return retVal

print "lenIter"
print lenIter("Adam")

def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    if aStr == "":
        return 0
    else:
        return 1 + lenRecur(aStr[1:])

print "lenRecur"
print lenRecur("hahahah")

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    num = len(aStr) / 2
    if char == aStr[num]:
        return True
    elif char < aStr[num] and len(aStr[:num]) > 1:
        return isIn(char, aStr[:num])
    elif char > aStr[num] and len(aStr[num:]) > 1:
        return isIn(char, aStr[num:])
    return False

print "isIn"
print isIn('j', "abcdefgh")

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    print "str1 : " + str1 + " str2 : " + str2
    if len(str1) != len(str2):
        return False
    if len(str1) == 1 and len(str2) == 1 and str1 == str2:
        return True
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False

print "semordnilap"
print semordnilap("nametag", "gateman")