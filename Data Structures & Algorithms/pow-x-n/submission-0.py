class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        neg = n<0
        for _ in range(abs(n)):
            res = res * x
        if neg: return 1/res
        return res