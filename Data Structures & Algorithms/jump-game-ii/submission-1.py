class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        res = 0
        r = 0
        l = 0

        while r < len(nums)-1:
            farthest = 0
            for k in range(l, r+1):
                farthest = max(farthest, k + nums[k])
                l += 1
            l = r+1
            r = farthest
            res += 1

        return res

