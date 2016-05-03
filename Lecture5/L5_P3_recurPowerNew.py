def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Recursive case 1: exp > 0 and even
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)

    # Otherwise, exp must be > 0 and odd, so use the second
    #  recursive case.
    return base * recurPowerNew(base, exp - 1)
