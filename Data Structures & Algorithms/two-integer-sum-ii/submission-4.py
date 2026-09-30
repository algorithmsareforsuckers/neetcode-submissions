class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while l < len(numbers) and r >= 0:
            curr = numbers[r] + numbers[l]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [l+1, r+1]