class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        mono = sorted(nums)
        res = []
        
        for i in range(len(nums)):
            if i > 0 and mono[i] == mono[i-1]:
                continue

            for j in range(i+1, len(nums)):
                if j > i+1 and mono[j] == mono[j-1]:
                    continue

                l = j+1
                r = len(nums)-1

                while l < r:
                    total = mono[i] + mono[j] + mono[l] + mono[r]
                    if total == target:
                        res.append([mono[i], mono[j], mono[l], mono[r]])
                        l += 1
                        r -= 1
                        while l < r and mono[l] == mono[l-1]:
                            l += 1
                        while l < r and mono[r] == mono[r+1]:
                            r -= 1
                    
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        
        return res

