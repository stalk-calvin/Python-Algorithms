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

    def msTodhms(self, ms):
        """
        Given ms, show its day, hour, min, second
        :return: d,h,m,s
        """
        s = ms / 1000
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        return d, h, m, s

    # recursive
    def combination_sum(self, n, t):
        if not n or not t:
            return []
        result = []
        if len(n) == 1:
            if n[0] == t:
                result.append(n[0])
            return result
        n = sorted(n)
        self.findSumRecursively(n, [], result, t, 0)
        return result

    def findSumRecursively(self, input, temp, result, target, start):
        if (target < 0):
            return
        elif (target == 0):
            result.append(list(temp))
        else:
            for i in range(start, len(input)):
                temp.append(input[i])
                self.findSumRecursively(input, temp, result, target - input[i], i)
                temp.pop()

    def compareBinToHex(self,b,h):
        bd=int(b,2)
        hd=int(h,16)
        return bd==hd

    def countCoin1d(self,S,m,n):
        table = [0 for k in range(n+1)]
        table[0] = 1
        for i in range(0,m):
            for j in range(S[i], n+1):
                table[j] += table[j-S[i]]

        return table[n]

    def countCoin2d(self, S, m, n):
        table = [[0 for x in range(m)] for x in range(n+1)]

        for i in range(m):
            table[0][i] = 1

        for i in range(1, n+1):
            for j in range(m):
                x = table[i-S[j]][j] if i-S[j] >= 0 else 0
                y = table[i][j-1] if j>=1 else 0
                table[i][j] = x + y

        return table[n][m-1]