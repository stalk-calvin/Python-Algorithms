class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            raise Exception('Empty Queue Exception')
        else:
            return self.items[0]

    def size(self):
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.items)>0:
            return self.dequeue()
        else:
            raise StopIteration

from collections import deque
class QueueUsingStacks():
    def __init__(self):
        self.stack1=deque()
        self.stack2=deque()

    def isEmpty(self):
        return not self.stack1 and not self.stack2

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        self.__rotateStack()
        return self.stack2.pop()

    def peek(self):
        self.__rotateStack()
        return self.stack2[-1]

    def __rotateStack(self):
        if (self.isEmpty()):
            raise Exception("queue is empty!")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def size(self):
        return len(self.stack1) + len(self.stack2)

class QueueUsingNodes():
    class QueueNode():
        def __init__(self,val,next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.length=0

    def enqueue(self, item):
        n=QueueUsingNodes.QueueNode(item)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            self.tail.next = n
            self.tail = n
        self.length+=1

    def dequeue(self):
        if (self.isEmpty()):
            raise Exception("queue is empty!")
        rv=None
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        self.length-=1
        return rv

    def peek(self):
        if (self.isEmpty()):
            raise Exception("queue is empty!")
        return self.head.val

    def isEmpty(self):
        return self.tail == None

    def size(self):
        return self.length