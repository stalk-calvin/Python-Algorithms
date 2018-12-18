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

    # def cantorSet(self,d,n):
    #     if n == 0:
    #         return (3 ** d) * '+'
    #     if d == 0:
    #         return '+'
    #     return self.cantorSet(d - 1, n - 1) + ' ' * (3 ** (d - 1)) + self.cantorSet(d - 1, n - 1)

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

    # def compareBinToHex(self,b,h):
    #     bd=int(b,2)
    #     hd=int(h,16)
    #     return bd==hd

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

    def computeMovingAverage(self, input, window_size):
        if input == None or window_size < 1:
            return 0
        elif len(input) == 1:
            return input[0]
        elif window_size > len(input):
            return -1

        result = []
        sum = 0
        for i in range(len(input)):
            if i < window_size:
                sum += input[i]
                result.append(int(sum / (i + 1)))
            else:
                remove_val = input[i - window_size]
                sum = (sum - remove_val) + input[i]
                result.append(int(sum / window_size))
        return result

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, (a % b))

    def count_ways(self, n):
        memo=[-1]*(n+1)
        return self.__count_ways(n, memo)

    def __count_ways(self, n, memo):
        if n < 0:
            return 0
        elif (n == 0):
            return 1
        elif memo[n] > -1:
            return memo[n]
        else:
            memo[n] = self.__count_ways(n-1, memo) + self.__count_ways(n-2, memo) + self.__count_ways(n-3, memo)
            return memo[n]

    def second_largest(self,x):
        largest=None
        second_largest=None
        for item in x:
            if largest==None:
                largest=item
            elif item > largest:
                second_largest=largest
                largest=item
            elif second_largest==None:
                second_largest=item

        return second_largest

    def subsets_of_set(self, data, index):
        result=[]
        if len(data) == index:
            result.append(list())
        else:
            result = self.subsets_of_set(data, index + 1)
            item = data[index]
            moresubsets=list(list())
            for subset in result:
                newsubset = list()
                for x in subset:
                    newsubset.append(x)
                newsubset.append(item)
                moresubsets.append(newsubset)
            for x in moresubsets:
                result.append(x)

        return result

    def swapMinMax(self, values):
        min_index = 0
        max_index = 0
        for i in range(1, len(values)):
            if values[i] < values[min_index]:
                min_index = i
            if values[i] > values[max_index]:
                max_index = i

        t = values[min_index]
        values[min_index] = values[max_index]
        values[max_index] = t

    def rotated_search(self, arr, key):
      if arr is None:
        return None
      if not isinstance(key, int):
        raise Exception("Search string can only be integer!")

      if arr[0] == key:
        return arr[0]
      elif arr[len(arr)-1]==key:
        return arr[len(arr)-1]

      l=0
      r=len(arr)
      while(l<=r):
        m=l+int((r-l)/2)
        if m==len(arr):
            break
        if key==arr[m]:
          return arr[m]
        elif arr[l] <= arr[m]:
          if arr[l] <= key and key < arr[m]:
            r=m-1
          else:
            l=m+1
        else:
          if (arr[m] < key and key <= arr[r]):
            l=m+1
          else:
            r=m-1

      return -1

    def binarySearchRecursive(self, arr, search, start, end):
        if arr and start <= end:
            m=start+int((end-start)/2)
            if search==arr[m]:
                 return arr[m]
            elif search < arr[m]:
                 return self.binarySearchRecursive(arr, search, start, m-1)
            else:
                 return self.binarySearchRecursive(arr, search, m+1, end)
        return -1

    def binarySearchIterative(self, arr, search):
        if arr is None:
            return None
        l = 0
        r = len(arr)-1
        while l <= r:
            m = (l+r) >> 1
            if search == arr[m]:
                return arr[m]
            elif search < arr[m]:
                r = m - 1
            else:
                l = m + 1
        return -1

    def sum_swap(self, a, b):
        if a is None or b is None:
            return None

        sum1=sum(a)
        sum2=sum(b)
        result=set()
        for x in a:
            for y in b:
                newsum1=sum1-x+y
                newsum2=sum2-y+x
                if newsum1==newsum2:
                    result.add((x,y))

        return result

    def sum_swap_target(self, a, b):
        if a is None or b is None:
            return None

        target=self.__ss_get_target(a,b)
        if not target:
            return None

        result = set()
        for x in a:
            for y in b:
                if x-y==target:
                    result.add((x,y))

        return result

    def __ss_get_target(self, a, b):
        sum1=sum(a)
        sum2=sum(b)
        if (sum1-sum2) % 2 != 0:
            return None
        return (sum1-sum2)/2

    def smallest_k(self, arr, k):
      if arr is None:
        return None

      arr.sort()

      if k > len(arr):
          k=len(arr)
      smallest=[None]*k
      for i in range(k):
        smallest[i] = arr[i]
      return smallest

    def is_magic(self, ans, arr, index, tmp):
        if (len(arr) > index):
            return self.is_magic(ans, arr, index + 1, tmp + arr[index]) or \
                   self.is_magic(ans, arr, index + 1, tmp - arr[index])
        elif ans == tmp:
         return True
        else:
         return False

    def peak_ram(self, A):
        times=dict()
        cur=0
        max=0
        for i in A:
            if i.start in times:
                old=times.get(i.start)
                new=old+i.ram
                times[i.start]=new
            else:
                times[i.start]=i.ram
            if i.end in times:
                old=times.get(i.end)
                new=old-i.ram
                times[i.end]=new
            else:
                times[i.end]=-i.ram

        t=sorted(times.items(), key=lambda x: x[0])

        for key,val in t:
            cur+=val
            if cur>max:
                max=cur

        return max
