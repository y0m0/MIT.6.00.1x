high = 100
low = 0
answer = False

print 'Please think of a number between 0 and 100!'

while answer is False:
    guess = (high + low)/2
    print 'is your secret number', str(guess)+'?'
    q1 = raw_input("Enter 'h' to indicate the guess is too high. "
     "Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if q1 == 'h':
        high = guess
        guess = (high + low)/2

    elif q1 == 'l':
        low = guess
        guess = (high + low)/2

    elif q1 == 'c':
        answer = True
        print 'Game over. Your secret number was:', str(guess)

    else:
        print 'Sorry, I did not understand your input.'
