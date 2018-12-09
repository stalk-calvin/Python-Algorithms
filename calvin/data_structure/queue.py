from calvin.data_structure.stack import Stack

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

class QueueUsingStacks():
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        self.__rotateStack()
        return self.stack2.pop()

    def peek(self):
        self.__rotateStack()
        return self.stack2.peek()

    def __rotateStack(self):
        if (self.isEmpty()):
            raise Exception("queue is empty!")

        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())

    def size(self):
        return self.stack1.size() + self.stack2.size()

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


class CircularQueue(object):
    def __init__(self, maxsize=8):
        self.max_size = maxsize
        self.queue_array = [None] * maxsize
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        if self.size >= self.max_size:
            raise Exception("Queue is full!")
        self.queue_array[self.tail] = item
        self.tail += 1
        self.tail = self.tail % self.max_size
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty!")
        rv = self.queue_array[self.head]
        self.head += 1
        self.head = self.head % self.max_size
        self.size -= 1
        return rv

    def peek(self):
        if (self.isEmpty()):
            raise Exception("Queue is empty!")

        return self.queue_array[self.head]

    def isEmpty(self):
        return self.size == 0

    def __repr__(self):
        r = ""
        c = self.head
        print("head: " + str(c))
        for i in range(self.size):
            index = (c + i) % self.max_size
            r += " " + str(self.queue_array[index])
        return r.lstrip()
