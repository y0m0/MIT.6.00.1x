def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    chyper = {}
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    for i in range(0,len(upper)):
        chyper[upper[i]] = upper[(i+shift)%len(upper)]
               

    for i in range (0,len(lower)):
        chyper[lower[i]] = lower[(i+shift)%len(lower)]


    return chyper
