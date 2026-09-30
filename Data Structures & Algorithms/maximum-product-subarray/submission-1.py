class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Bottom up, keep track of largest negative and largest positive
        best = 0
        best_neg = 0
        best_pos = 0
        zero_seen = False

        for num in nums:
            if num < 0:
                tmp = best_pos
                best_pos = best_neg * num
                best_neg = num * max(1,tmp)
            if num > 0:
                best_pos = max(num, best_pos * num)
                best_neg *= num
            if num == 0:
                zero_seen = True
                best_pos = 0
                best_neg = 0
            best = max(best, best_pos)
            
        if not zero_seen and best == 0:
            return max(nums)
        return best
