testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def add1(x):
    return  1 + x


applyToEach(testList, add1)

print testList
