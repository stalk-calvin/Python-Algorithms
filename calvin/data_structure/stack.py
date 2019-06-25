class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception('Empty Stack Exception')
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __iter__(self):
        for x in range(self.size()):
            yield self.pop()

    def __next__(self):
        if len(self.items)>0:
            return self.pop()
        else:
            raise StopIteration

    def sort(self, stack):
        tracker=Stack()
        while not stack.isEmpty():
            t=stack.pop()
            while not tracker.isEmpty() and t>tracker.peek():
                stack.push(tracker.pop())
            tracker.push(t)

        return tracker

    def sortStack(self, stack):
        if (not stack.isEmpty()):
            value = stack.pop()
            self.sortStack(stack)
            self.insert(stack, value)

    def insert(self, stack, value):
        if (stack.isEmpty() or value < stack.peek()):
            stack.push(value)
        else:
            temp = stack.pop()
            self.insert(stack, value)
            stack.push(temp)

class StackUsingQueue:
    def __init__(self):
        from calvin.data_structure.queue import Queue
        self.queue = Queue()

    def isEmpty(self):
        return self.queue.isEmpty()

    def push(self, item):
        self.queue.enqueue(item)
        for i in range(self.size() - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty!")

        return self.queue.dequeue()

    def peek(self):
        if self.isEmpty():
            raise Exception("stack is empty!")

        return self.queue.peek()

    def size(self):
        return self.queue.size()

class StackUsingNodes():
    class StackNode():
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

    def __init__(self, capacity=None):
        self.head = None
        self.length = 0
        self.capacity = capacity

    def is_full(self):
        return self.capacity == self.length

    def push(self, item):
        if (self.is_full()):
            return False
        n=StackUsingNodes.StackNode(item)
        n.next = self.head
        self.head = n
        self.length+=1
        return True

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Stack!")

        rv=self.head.val
        self.head = self.head.next
        self.length -= 1
        return rv

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Stack!")

        return self.head.val

    def isEmpty(self):
        return self.head is None

    def size(self):
        if self.head is None:
            return 0
        return self.length

class ThreeStacks(object):
    def __init__(self, stack_size=3, number_of_stacks=3):
        self.capacity = stack_size
        self.items= [None] * (stack_size * number_of_stacks)
        self.sizes= [0] * number_of_stacks

    def push(self, stack_num, item):
        if self.isFull(stack_num):
            raise Exception ("Full Stack!")

        self.sizes[stack_num]+=1
        self.items[self.index_of_top(stack_num)] = item

    def pop(self,stack_num):
        if self.isEmpty(stack_num):
            raise Exception("Empty Stack!")

        top_index = self.index_of_top(stack_num)
        value = self.items[top_index]
        self.items[top_index] = None
        self.sizes[stack_num]-=1
        return value

    def peek(self, stack_num):
        if self.isEmpty(stack_num):
            raise Exception("Empty Stack!")

        return self.items[self.index_of_top(stack_num)]

    def isEmpty(self, stack_num):
        return self.sizes[stack_num] == 0

    def isFull(self, stack_num):
        return stack_num >= self.capacity or self.sizes[stack_num] == self.capacity

    def index_of_top(self, stack_num):
        offset=stack_num*self.capacity
        size = self.sizes[stack_num]
        return offset + size - 1

class StackMin(object):
    class MinNode(object):
        def __init__(self, val, min):
            self.val = val
            self.min = min if min else val

    def __init__(self):
        self.items = []

    def push(self, item):
        min=self.peek().min if self.items and self.peek().min < item else item
        mn=StackMin.MinNode(item,min)
        self.items.append(mn)

    def pop(self):
        if self.items:
            mn=self.items.pop()
            return mn.val
        else:
            raise Exception("Stack Empty!")

    def peek(self):
        if self.items:
            return self.items[len(self.items) - 1]
        else:
            raise Exception("Stack Empty!")

    def min(self):
        if self.items:
            return self.peek().min
        else:
            raise Exception("Stack Empty!")

class SetOfStacks(object):
    def __init__(self, capacity=3):
        self.stacks = []
        self.capacity = capacity

    def get_last_stack(self):
        if (len(self.stacks)==0):
            return None
        return self.stacks[len(self.stacks)-1]

    def push(self, item):
        last = self.get_last_stack()
        if last is None or last.is_full():
            # create a new stack
            stack=StackUsingNodes(self.capacity)
            stack.push(item)
            self.stacks.append(stack)
        else:
            #add to last
            last.push(item)

    def pop(self):
        last = self.get_last_stack()
        if last==None:
            raise Exception("Stack is Empty!")

        rv=last.pop()
        if last.length==0:
            self.stacks.pop()

    def isEmpty(self):
        last=self.get_last_stack()
        return last is None or last.isEmpty()


