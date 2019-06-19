class ListNode(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def getNodes(self,r):
        if self is None:
            return r

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

    def append(self, element, next=None):
        temp = ListNode(element, next)
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
        n=self.head
        if n.value==value_to_remove:
            self.head = self.head.next

        while n.next:
            if n.next.value == value_to_remove:
                n.next = n.next.next
                return self.head
            n=n.next

        return self.head

    def remove_dupes(self):
        n=self.head
        t=set()
        p=None
        while n:
            if n.value in t:
                p.next=n.next
            else:
                t.add(n.value)
                p=n
            n=n.next
        return self.head

    def printKthLastRecursive(self, head, k, result):
        if head is None:
            return 0

        index = self.printKthLastRecursive(head.next, k, result) + 1

        if (index == k):
            result.append(head.value)

        return index

    def getKthLastUsingNodes(self, head, k):
        p1=head
        p2=head
        for i in range(k):
            if p1 is None:
                return None
            p1=p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2

    def delete_middle_node(self, n):
        if n is None:
            return False
        if n.next is None:
            #remove tail = unsupported (no reference to tail)
            return False

        next = n.next
        n.value = next.value
        n.next = next.next

        return True

    def partition(self, head, val):
        before=None
        after=None
        while head:
            next=head.next
            if head.value < val:
                head.next=before
                before=head
            else:
                head.next=after
                after=head
            head=next

        if before==None:
            return after

        node=before
        while before.next:
            before=before.next
        before.next=after

        return node

    def sum_list(self, l1, l2, c):
        if l1 is None and l2==None and c==0:
           return None

        result=ListNode()
        val=c
        if l1 != None:
            val+=l1.value
        if l2 != None:
            val+=l2.value

        result.value = val % 10
        if (l1 != None or l2 != None):
            more = self.sum_list(l1.next if l1 else None, l2.next if l2 else None, 1 if val >= 10 else 0)
            result.next = more

        return result

    def palindrome(self,l):
        from collections import deque
        t=deque()
        c=l
        size = 0
        while c:
            size+=1
            c=c.next
        length = int(size/2)
        for i in range(length):
            t.append(l.value)
            l = l.next

        if size % 2 != 0:
            l = l.next

        while l:
            if l.value != t.pop():
                return False
            l = l.next

        return len(t) == 0

    def intersection(self, l1, l2):
        t=set()
        while l1:
            t.add(l1)
            l1 = l1.next

        while l2:
            if l2 in t:
                return l2
            l2 = l2.next

        return None

    def loop_detection(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if(slow is fast):
                break

        slow=self.head
        while slow != fast:
            slow=slow.next
            fast=fast.next

        return fast

class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class SortedLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def insert(self, n):
        curr=self.head
        if curr is None:
            nn= ListNode(n)
            self.head=nn
            return

        if curr.value > n:
            nn=ListNode(n, next=curr)
            self.head=nn
            return

        while curr.next is not None:
            if curr.next.value > n:
                break
            curr=curr.next

        nn=ListNode(n, next=curr.next)
        curr.next=nn
        self.size += 1

        return

    def delete_head_node(self):
        nn=self.head
        self.head=nn.next
        self.size-=1

    def search_node(self, n):
        if self.head is None:
            return None

        nn = self.head
        while nn:
            if nn.value == n:
                return nn
            nn = nn.next

        return None

    def list_to_bst(self):
        if self.head is None:
            return None
        return self.to_bst(self.head, None)

    def to_bst(self, head, tail):
        if head is tail:
            return None

        fast=head
        slow=head

        while fast is not tail and fast.next is not tail:
            fast=fast.next.next
            slow=slow.next

        current=TreeNode(slow.value)
        current.left=self.to_bst(head, slow)
        current.right=self.to_bst(slow.next, tail)
        return current

    def __repr__(self):
         return self.__helper(self.head, "").lstrip()

    def __helper(self, current, result):
        if current is None:
            return result
        result += ' ' + str(current.value)
        return self.__helper(current.next, result)