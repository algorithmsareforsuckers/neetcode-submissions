class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since input is sorted, start l and r and then move in whichever way is needed
        l = 0
        r = len(numbers) - 1

        curr = numbers[l] + numbers[r]
        while curr != target:
            if curr > target:
                r -= 1
            else:
                l += 1
            curr = numbers[l] + numbers[r]

        return [l+1, r+1]