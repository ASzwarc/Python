from random import randint

def diceRolling(repetitions, sidesOnDice, results):
    percentageResult = []
    for i in range(repetitions) :
        score = randint(1, sidesOnDice)
        try :
            results[score] += 1
        except IndexError :
            print "Index error"
            break
        print score
    for x in range(len(results)):
        percentageResult.append(results[x] / float(repetitions))
    printSummaryOfGame(results, percentageResult)

def printSummaryOfGame(results, percentageResult):
    """ Function that prints summary of one game
    """
    print "Summary of this run : "
    for x in range(len(results)):
        scoreStr = str(x) + " was scored " + str(results[x])
        if ( results[x] == 1 ):
            scoreStr += " time"
        else:
            scoreStr += " times"
        print scoreStr
    print "Summary in percents"
    for x in range(len(results)):
        print "Number " + str(x) + " was scored in " + str(percentageResult[x]) + " % of throws"

def manageOneRun() :
    """ Function that prints user's menu and manages input from user
    """
    try :
        sidesOnDice = int(raw_input("Tell me the number of sides : "))
        repetitions = int(raw_input("How many rolls : "))
    except ValueError :
        print "Value error, using default values : 1, 1"
        sidesOnDice = 1
        repetitions = 1
    results = [0] * (sidesOnDice + 1)
    diceRolling(repetitions, sidesOnDice, results)

__author__ = 'Adam'
runProgram = True
while runProgram :
    print "q - end program\nn - new run with new parameters"
    decision = raw_input("Your decision : ")
    if (decision == "n"):
        manageOneRun()
    elif (decision == "q") :
        runProgram = False
    else :
        print "You choose wrong option, quitting ..."
        runProgram = False

print "Program finished working"

