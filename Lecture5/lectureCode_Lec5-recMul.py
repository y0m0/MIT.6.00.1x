def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)

    
