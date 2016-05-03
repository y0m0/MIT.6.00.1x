# In your Queue class, you will need three methods:
# 1- __init__: initialize your Queue
#   (think: how will you store the queue's elements? You'll need to initialize
#   an appropriate object attribute in this method)
#
# 2- insert: inserts one element in your Queue
#
# 3- remove: removes (or 'pops') one element from your Queue and returns it.
#    If the queue is empty, raises a ValueError.






class Queue(object):

    def __init__(self):
        self.queue = list()

    def insert(self, i):
        if i not in self.queue:
            self.queue.append(i)

    def remove(self):
        try:
            return self.queue.pop(0)
        except:
            raise ValueError('no items in the queue')

    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(i) for i in self.queue]) + '}'

q1 = Queue()
q1.insert(1)
q1.insert(2)
q1.insert(3)
q1.insert(4)
print q1

q1.remove()
q1.remove()
print q1
q1.remove()
q1.remove()
print q1

q1.remove()