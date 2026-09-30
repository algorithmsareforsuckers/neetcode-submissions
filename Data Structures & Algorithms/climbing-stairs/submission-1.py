class Solution:
    def climbStairs(self, n: int) -> int:
        # 2 -> 2, 3 -> 3, the first step for n > 3 is either 1 or 2

        if n == 1:
            return 1
        if n == 2:
            return 2
        
        prev_two = [2,1]
        curr = 2
        while curr < n:
            tmp = prev_two[0] + prev_two[1]
            prev_two = [tmp,prev_two[0]]
            curr += 1

        return prev_two[0]