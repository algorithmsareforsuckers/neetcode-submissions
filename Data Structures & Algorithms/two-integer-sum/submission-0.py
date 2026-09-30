class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i, n in enumerate(nums):
            rem = target - n
            if rem in seen:
                return [seen[rem], i]
            seen[n] = i

        return [0,1]


        