class SortAlgorithms(object):
    def __swap(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    def bubble_sort(self, A):
        swapped=False
        for i in range(len(A)-1):
            if swapped:
                break
            swapped = True
            for j in range(len(A)-i-1):
                if A[j] > A[j+1]:
                    self.__swap(A, j+1, j)
                    swapped=False

    def selection_sort(self, A):
      if A is None or len(A) < 2:
        return A

      for i in range(len(A)):
        min=(A[i],i)
        for j in range(i+1,len(A)):
          if A[j] < min[0]:
            min=(A[j],j)

        if min[0] != A[i]:
          #swap with current i
          tmp=min[0]
          A[min[1]]=A[i]
          A[i]=tmp

      return A

    def insertion_sort(self, A):
        if A is None or len(A) < 2:
            return A

        for i in range(len(A)):
            current = A[i]
            j = i - 1
            while j >= 0 and A[j] > current:
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = current

        return A

    def merge_sort(self, items, start, end):
        if start < end:
            m = int(start + (end - start) / 2)
            self.merge_sort(items, start, m)
            self.merge_sort(items, m + 1, end)
            self.merge(items, start, m, end)

    def merge(self, items, start, middle, end):
        # find size first
        n1 = middle - start + 1
        n2 = end - middle
        left = [None] * n1
        right = [None] * n2
        for i in range(len(left)):
            left[i] = items[start + i]
        for j in range(len(right)):
            right[j] = items[middle + 1 + j]
        i, j = 0, 0
        print(left, right)
        for k in range(start, end + 1):
            print(k, i, j, start, end)
            if ((j >= n2) or (i < n1 and left[i] <= right[j])):
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j += 1

    def quick_sort(self, A, start, end):
        if A is None:
            return None
        if start < end:
            p=self.__partition(A, start, end)
            self.quick_sort(A, start, p-1)
            self.quick_sort(A, p+1, end)

    def __partition(self, A, start, end):
        pivot=A[end]
        i=start
        for j in range(start,end):
            if A[j] <= pivot:
                self.__swap(A, i, j)
                i+=1
        self.__swap(A, i, end)
        return i

    def counting_sort(self, n):
        temp=[0]*15

        for i in range(len(n)):
            temp[n[i]] = temp[n[i]]+1

        curr=0
        for i in range(len(temp)):
            for j in range(temp[i]):
                n[curr] = i
                curr+=1


