def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
        
    if a > b and a / b != 0:
        return gcdIter(a-b,b)
    elif b > a and b / a != 0:
        return gcdIter(a,b-a)
    else:
        return a

    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)
