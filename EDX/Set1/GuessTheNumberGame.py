__author__ = 'aszwarc'

guess = 50
low = 0
high = 100
print "Please think of a number between 0 and 100!"

while True:
    print "Is your secret number " + str(guess) + "?"
    answer = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess "
                       "is too low. Enter 'c' to indicate I guessed correctly. ")
    if answer == 'h':
        high = guess
        guess = (high + low) / 2
    elif answer == 'l':
        low = guess
        guess = (high + low) / 2
    elif answer == 'c':
        print "Game over. Your secret number was: " + str(guess)
        break
    else:
        print "Sorry, I did not understand your input."