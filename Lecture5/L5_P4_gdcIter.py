def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    while a != b:
        if a > b:
           a = a - b
        else:
           b = b - a
    return a

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue
