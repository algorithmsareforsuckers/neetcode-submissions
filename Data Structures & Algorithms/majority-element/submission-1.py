class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        count = 1

        for n in nums[1:]:
            if n == cand:
                count += 1
            else:
                count -= 1

            if count == 0:
                cand = n
                count = 1
        
        return cand
