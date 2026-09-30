class Solution:
    def isHappy(self, n: int) -> bool:
        def square_digits(n, i):
            res = 0
            for power in range(i):
                curr = n // (10**(power)) # ignore low digits
                curr = curr % (10) # ignore higher digits
                res += curr**2
            return res


        counts = defaultdict(int)
        val = n
        counts[n] = 1
        while val != 1:
            val = square_digits(val, len(str(abs(val))))
            counts[val] += 1
            if counts[val] > 1:
                return False
        return True
