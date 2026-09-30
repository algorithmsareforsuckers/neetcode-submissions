class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Because array is sorted, if we put one pointer at beg, one at end,
        # when too large move right - 1, and when too small move left.

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        
        return [-1, -1]