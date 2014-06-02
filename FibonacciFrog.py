__author__ = 'Adam'

def solution(A):
    lastValue = len(A) + 1
    calculateFibonacci(lastValue)
    occurencesOfOne = [i for i, val in enumerate(A) if val == 1]


def calculateFibonacci(lastValue):
    results = [0, 1]
    value = 0
    while value <= lastValue:
        value = results[-1] + results[-2]
        if (value <= lastValue):
            results.append(value)
    return results
