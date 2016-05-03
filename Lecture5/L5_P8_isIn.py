def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    # Base case: If aStr is empty, we did not find the char.
    if aStr == '':
        return False
    
    # Base case: if aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
        return char == aStr
    
    middle = aStr[len(aStr)/2]
    if char == middle:
        return True

    # Recursive case: If the test character is bigger than the middle 
    #  character, recursively search on the first half of aStr

    if char > middle:
        return  isIn(char,aStr[len(aStr)/2:])

    # Otherwise the test character is smaller than the middle 
    # character, recursively search on the first half of aStr
    else:
        return isIn(char,aStr[:len(aStr)/2])
