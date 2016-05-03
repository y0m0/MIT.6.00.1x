import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name

# me = Person("William Eric Grimson")
# print me
# me.getLastName()
# me.setBirthday(1,2,1927)
# me.getAge()
# her = Person("Cher")
# her.getLastName()
# plist = [me, her]
# for p in plist: print p
# plist.sort()
# for p in plist: print p

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

# p1 = MITPerson('Eric')
# p2 = MITPerson('John')
# p3 = MITPerson('John')
# p4 = Person('John')

# print p1

# p1.getIdNum()
# p2.getIdNum()
# p1 < p2
# p3 < p2
# p4 < p1

# p1 < p4


class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)

#s1 = UG('Fred', 2016)
#s2 = Grad('Angela')
#isStudent(s1)
#isStudent(s2)

class TransferStudent(MITPerson):
    pass

# go back and define
# class Student(MITPerson)
# change inheritance for UG, Grad and TransferStudent
# change def isStudent(obj):
#            return isinstance(obj, Student)


