class Numbers(object):
    """
    Implementation on String Manipulation
    """
    def fib(self, n):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if n == 0: return 0
        elif n == 1: return 1
        else: return self.fib(n-1)+self.fib(n-2)

    def fib2(self, n):
        if (n == 1 or n == 2):
            return 1
        n0 = 1
        n1 = 1
        for i in range(2, n):
            temp = n1
            n1 += n0
            n0 = temp
        return n1

    table = [0, 1]
    def fib3(self, n):
        if (0 <= n < len(self.table)):
            return self.table[n]

        self.table.append(self.fib3(n - 1) + self.fib3(n - 2));
        return self.table[n]
