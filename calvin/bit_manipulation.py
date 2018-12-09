class BitManipulation(object):
    def merge2bits(self, n, m, i, j):
        if i >= 32 or j < i:
            return 0

        allOnes = ~0

        left = allOnes << (j + 1)  # 1111000
        right = (1 << i) - 1  # 00001111
        mask = left | right

        n_cleared = n & mask
        m_shifted = m << i

        return n_cleared | m_shifted

    def print_binary(self, num):
        if (num >= 1 or num <= 0):
            return "ERROR"

        binary = []
        binary.append('.')
        while num > 0:
            if (len(binary) > 32):
                return "ERROR"

            r = num * 2
            if r >= 1:
                binary.append(1)
                num = r - 1
            else:
                binary.append(0)
                num = r
        return ''.join(str(i) for i in binary)

    def is_one(self, num, i):
        return (num & (1 << i)) != 0

    def longest_sequence(self, n):
        max_seq = 0

        for i in range(32):
            max_seq = max(max_seq, self.longest_sequence_of_1s(n, i))

        return max_seq

    def longest_sequence_of_1s(self, n, indexToIgnore):
        high = 0
        counter = 0

        for i in range(32):
            if i == indexToIgnore or self.is_one(n, i):
                counter += 1
                high = max(counter, high)
            else:
                counter = 0

        return high
