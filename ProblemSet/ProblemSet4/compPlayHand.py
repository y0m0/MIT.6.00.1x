def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print( 'Current Hand: '),
        displayHand(hand)
        # Computer choose best word possible
        word = (compChooseWord(hand, wordList, n))
        # If there is no more possible word with the given hand:
        if word is None:
            # End the game (break out of the loop)
            print "Total score:", score, "points."
            print
            break

        else:
            # print how many points the word earned, and the updated total score
            score += getWordScore(word, n)
            print '"'+word+'"', "earned", getWordScore(word, n), "points. Total:", score, "points"
            print
            # Update the hand
            hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print "Total score:", score, "points."
