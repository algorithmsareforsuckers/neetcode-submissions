class Solution:
    def trap(self, height: List[int]) -> int:
        # go left to right until max, then right to left until max

        mx_ind = 0
        for i, h in enumerate(height):
            if h > height[mx_ind]: mx_ind = i

        best = 0
        r,l,curr = 1,0,0
        while r <= mx_ind:
            if height[r] >= height[l]:
                best += curr
                curr = 0

                l = r
            
            else:
                curr += height[l] - height[r]
            
            r += 1
        
        r = len(height)-1
        l = len(height)-2
        curr = 0
        while l >= mx_ind:
            if height[l] >= height[r]:
                best += curr
                curr = 0
                r = l
            else:
                curr += height[r] - height[l]
            l -= 1
        

        return best