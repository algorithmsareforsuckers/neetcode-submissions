class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        best_neg = 1
        best_pos = 1

        for num in nums:
            tmp = best_neg * num
            best_neg = min(num*best_neg, num*best_pos, num)
            best_pos = max(tmp, num*best_pos, num)
            best = max(best, best_pos)
        return best