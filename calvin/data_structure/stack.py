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