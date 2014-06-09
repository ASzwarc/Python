__author__ = 'Adam'

import sys

if len(sys.argv) > 1 :
    inputFile = open(str(sys.argv[1]), 'r')
else :
    print "You should specify file to open"

for line in inputFile :
    print line




