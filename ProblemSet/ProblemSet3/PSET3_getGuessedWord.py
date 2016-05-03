def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    word = ''

    for i in secretWord:
        if i not in lettersGuessed:
            word += ' _ '
        else:
            word += i
    return word

print getGuessedWord('albero',['c'])