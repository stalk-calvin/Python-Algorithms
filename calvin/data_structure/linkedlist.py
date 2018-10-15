class ListNode(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def getNodes(self,r):
        if self.next:
            self.next.getNodes(r)
        r.insert(0,self.value)
        return r

    def __repr__(self):
        return repr(self.value)

class LinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ','.join(nodes) + ']'

    def prepend(self, element):
        self.head = ListNode(value=element, next=self.head)

    def append(self, element):
        temp = ListNode(element)
        if not self.head:
            self.head = temp
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = temp

    def find(self, key):
        c = self.head
        while c and c.value != key:
            c = c.next
        return c # None if not found

    def reverse(self):
        c = self.head
        prev_node = None
        next_node = None
        while c:
            next_node = c.next
            c.next = prev_node
            prev_node = c
            c = next_node
        self.head = prev_node

    #O(n)
    def delete_node_by_value(self, value_to_remove):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.value == value_to_remove:
                if previous_node is None:
                    new_head = current_node.next
                    current_node.next = None
                    self.head = new_head
                    return new_head
                previous_node.next = current_node.next
                return self.head
            previous_node = current_node
            current_node = current_node.next
        return self.head #not found