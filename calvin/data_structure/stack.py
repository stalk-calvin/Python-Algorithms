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
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.items)>0:
            return self.pop()
        else:
            raise StopIteration

from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def isEmpty(self):
        return not self.queue

    def push(self, item):
        self.queue.append(item)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty!")

        return self.queue.popleft()

    def peek(self):
        if self.isEmpty():
            raise Exception("stack is empty!")

        return self.queue[0]

    def size(self):
        return len(self.queue)