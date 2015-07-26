__author__ = 'aszwarc'

s = 'azcbobobegghakl'

position = 0
count = 0
while position <= (len(s) - 2):
    temp = s.find('bob', position)
    if temp == -1:
        position += 1
    else:
        position = temp + 1
        count += 1
print "Number of times bob occurs is: " + str(count)
