import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        mat = np.array([[1,1],[1,0]])
        res = np.linalg.matrix_power(mat, n-1)
        return int(res[0].sum())