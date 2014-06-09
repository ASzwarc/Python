__author__ = 'Adam'

import sys
import fileinput

if len(sys.argv) < 1 :
    print "You should specify file to open"
else :
    for line in fileinput.input( str(sys.argv[1]) ) :
        if fileinput.isfirstline() :
            print "It's first line"
        print line





