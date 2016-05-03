# applyToEach

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.4]

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

applyToEach(L, fact)
print(L)

applyToEach(L, fib)
print(L)
