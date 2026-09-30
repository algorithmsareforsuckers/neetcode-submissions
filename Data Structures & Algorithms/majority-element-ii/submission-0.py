class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = [float("inf"),0]
        c2 = [float("inf"),0]

        for n in nums:
            if n == c1[0]:
                c1[1] += 1
            elif n == c2[0]:
                c2[1] += 1
            elif c1[1] == 0:
                c1 = [n,1]
            elif c2[1] == 0:
                c2 = [n,1]
            else:
                c1[1] -= 1
                c2[1] -= 1
            

        # Check if these numbers actually appear enough
        req = len(nums) // 3
        c1[1] = 0
        c2[1] = 0
        for n in nums:
            if n == c1[0]: c1[1] += 1
            if n == c2[0]: c2[1] += 1
        res = []
        if c1[1] > req: res.append(c1[0])
        if c2[1] > req: res.append(c2[0])

        return res

