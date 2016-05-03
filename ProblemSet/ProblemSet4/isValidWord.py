def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    tempHand = hand.copy()
    if len(word) > 0 and word in wordList:
        for letter in word:
            if letter not in tempHand or tempHand[letter] <= 0:
                return False
            else:
                tempHand[letter] = tempHand.get(letter, 0) - 1
        return True
    return False
