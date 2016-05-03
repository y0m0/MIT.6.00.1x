def getSubjectStats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)]
            for elt in subject]

def dotProduct(a,b):
    result = 0.0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result

def avg(grades, weights):
    return dotProduct(grades, weights)/len(grades)


def avg(grades, weights):
    try:
        return dotProduct(grades, weights)/len(grades)
    except ZeroDivisionError:
        print 'no grades data'

def avg(grades, weights):
    try:
        return dotProduct(grades, weights)/len(grades)
    except ZeroDivisionError:
        print 'no grades data'
        return 0.0

def convertLetterGrade(grade):
    if type(grade) == int:
        return grade
    elif grade == 'A':
        return 90.0
    elif grade == 'B':
        return 80.0
    elif grade == 'C':
        return 70.0
    elif grade == 'D':
        return 60.0
    else:
        return 50.0

def avg(grades, weights):
    try:
        return dotProduct(grades, weights)/len(grades)
    except ZeroDivisionError:
        print 'no grades data'
        return 0.0
    except TypeError:
        newgrades = [convertLetterGrade(elt) for elt in grades]
        return dotProduct(newgrades, weights)/len(newgrades)

def avg(grades, weights):
    assert not len(grades) == 0, 'no grades data'
    newgrades = [convertLetterGrade(elt) for elt in grades]
    return dotProduct(newgrades, weights)/len(newgrades)

def avg(grades, weights):
    assert not len(grades) == 0, 'no grades data'
    assert len(grades) == len(weights), 'wrong number grades'
    newgrades = [convertLetterGrade(elt) for elt in grades]
    result = dotProduct(newgrades, weights)/len(newgrades)
    assert 0.0 <= result <= 100.0, 'grade exceeds limits'
    return result


test = [[['fred', 'flintstone'], [10.0, 5.0, 85.0]],
        [['barney', 'rubble'], [10.0, 8.0, 74.0]],
        [['wilma', 'flintstone'], [8.0, 10.0, 96.0]],
        [['dino'], []]]

weights = [.3, .2, .5]

weights1 = [.15, .1, .25, .25]

test1 = [[['fred', 'flintstone'], [10.0, 5.0, 85.0, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']],
         [['dino'], []]]

test2 = [[['fred', 'flintstone'], [10.0, 5.0, 8500, 'D']],
         [['barney', 'rubble'], [10.0, 8.0, 74.0, 'B']],
         [['wilma', 'flintstone'], [8.0, 10.0, 96.0, 'A']]]

