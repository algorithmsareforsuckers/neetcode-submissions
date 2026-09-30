class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0

        hw = []
        for i, height in enumerate(heights):
            
            start_ind = i
            while hw and height <= hw[-1][0]:
                start_ind = hw[-1][1]
                best = max(best, hw[-1][0]*(i-hw[-1][1]))
                hw.pop()
            
            hw.append([height, start_ind])
            
        for h, si in hw:
            best = max(best, h*(len(heights)-si))
        return best