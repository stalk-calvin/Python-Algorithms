class Two_2(object):
    def kth_to_last(self, head, k):
        if k < 1:
            return head

        p1 = head
        p2 = head

        for i in range(k):
            if p1 is None:
                return None
            p1 = p1.next

        while (p1 is not None):
            p1 = p1.next
            p2 = p2.next

        return p2