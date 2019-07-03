class Two_1(object):
    def remove_dupe(self, head):
        s = set()
        previous = None
        while (head != None):
            if head.value in s:
                previous.next = head.next
            else:
                s.add(head.value)
                previous = head
            head = head.next