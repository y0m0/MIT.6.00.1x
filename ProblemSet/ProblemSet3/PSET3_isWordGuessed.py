def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

print isWordGuessed('albero',['k','a','b','w','c','r','o'])