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

        self.table.append(self.fib3(n - 1) + self.fib3(n - 2))
        return self.table[n]

    def bullsAndCows(self, secret, guess):
        bulls = 0
        cows = 0
        numbers = [0] * 10
        for x in range(len(secret)):
            s = int(secret[x])
            g = int(guess[x])
            if (s == g):
                bulls += 1
            else:
                if (numbers[s] and numbers[s] < 0): cows += 1
                if (numbers[g] and numbers[g] > 0): cows += 1
                numbers[s] += 1
                numbers[g] -= 1

        return str(bulls) + "A" + str(cows) + "B"

    def toBinaryNumber(self, x, y):
        return ''.join('10'[a + b < '11'] for a, b in zip(x, y))

    def sortNumbersBetweenSigns(self, s, sign):
        return sign.join(sorted(s.split(sign)))

    def cantorSet(self,d,n):
        if n == 0:
            return (3 ** d) * '+'
        if d == 0:
            return '+'
        return self.cantorSet(d - 1, n - 1) + ' ' * (3 ** (d - 1)) + self.cantorSet(d - 1, n - 1)