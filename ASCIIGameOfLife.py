__author__ = 'Adam'

import sys
import fileinput

class GameOfLine( object ):

    def __init__(self, iterations = 0, X = 0, Y = 0):
        self.__iterations = iterations
        self.__X = X
        self.__Y = Y
        self.__matrix = [["." for x in xrange(X)] for y in xrange(Y)]

    def setParams(self, iterations, X, Y):
        self.__iterations = iterations
        self.__X = X
        self.__Y = Y
        self.__matrix = [["." for x in xrange(X)] for y in xrange(Y)]

    def printBoard(self):
        print "\n".join(" ".join(str(element) for element in row) for row in self.__matrix)

    def __str__(self):
        return "iterations : %d, board : %dx%d" % (self.__iterations, self.__X, self.__Y)

if __name__ == "__main__" :
    if len(sys.argv) < 1 :
        print "You should specify file to open"
    else :
        game = GameOfLine()
        for line in fileinput.input( str(sys.argv[1]) ) :
            if fileinput.isfirstline() :
                inputParams = line.split()
                game.setParams( int(inputParams[0]), int(inputParams[1]), int(inputParams[2]) )
                print (game)
            else :
                print line
        print "Initialized board"
        game.printBoard()




