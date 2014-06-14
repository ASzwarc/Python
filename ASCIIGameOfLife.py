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

    def initializeLineOfBoard(self, inputLine, boardRow) :
        #     TODO @aszwarc : add proper error handling in case if input line is empty
        self.__matrix[boardRow] = inputLine

    def analyzeStateOfCell(self, x, y):
        numberOfOnNeighbours = 0
        print "Checking element [" + str(y) + ", " + str(x) + "]"
        for col in range(y - 1, y + 1):
            for row in range(x - 1, x + 1):
                if (self.__matrix[col][row] == "#"):
                    print "Element [" + str(col) + ", " + str(row) + "] is ON"
                    numberOfOnNeighbours += 1
                else:
                    print "Element [" + str(col) + ", " + str(row) + "] is OFF"
        if (self.__matrix[y][x] == "." and numberOfOnNeighbours == 3):
            print "Turning ON point : " + str(y) + ", " + str(x)
            self.__matrix[y][x].replace(".", "#")
        elif (self.__matrix[y][x] == "#" and numberOfOnNeighbours < 2):
            print "Underpopulation - Turning OFF point : " + str(y) + ", " + str(x)
            self.__matrix[y][x].replace("#", ".")
        elif (self.__matrix[y][x] == "#" and numberOfOnNeighbours > 3):
            print "Overpopulation - Turning OFF point : " + str(y) + ", " + str(x)
            self.__matrix[y][x].replace("#", ".")

    def runOneIteration(self):
        for col in xrange(self.__Y):
            for row in xrange(self.__X):
                self.analyzeStateOfCell(row, col)

    def __str__(self):
        return "iterations : %d, board : %dx%d" % (self.__iterations, self.__X, self.__Y)

def readGameBoardFromFileAtInput():
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
                game.initializeLineOfBoard(line, fileinput.filelineno() - 2)
        print "Initialized board"
        game.printBoard()
        print "First iteration \n : "
        game.runOneIteration()
        print "---------------------------"
        game.printBoard()

if __name__ == "__main__" :
    readGameBoardFromFileAtInput()





