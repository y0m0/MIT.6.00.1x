class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob: a Frob with no links
    This procedure appropriately insert newFrob into the linked list
    that atMe is part of.
    """
    #NewFrob comes before atMe.
    if newFrob.name < atMe.name:
        if atMe.before is not None and atMe.before == newFrob.before:
            newFrob.after = atMe
            atMe.before = newFrob
            newFrob.before.after = newFrob
        elif atMe.before is None:
            atMe.before = newFrob
            newFrob.after = atMe
        else:
            newFrob.after = atMe
            insert(atMe.before, newFrob)

    #NewFrob comes after atMe.
    elif newFrob.name > atMe.name:
        if atMe.after is not None and atMe.after == newFrob.after:
            newFrob.before = atMe
            atMe.after = newFrob
            newFrob.after.before = newFrob
        elif atMe.after is None:
            atMe.after = newFrob
            newFrob.before = atMe
        else:
            newFrob.before = atMe
            insert(atMe.after, newFrob)

    #NewFrob has the same name as atMe.
    else:
        newFrob.after = atMe.after
        atMe.after = newFrob
        newFrob.before = atMe
        if newFrob.after is not None:
            newFrob.after.before = newFrob


def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    if start.before is not None:
        return findFront(start.before)
    else:
        return start

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
