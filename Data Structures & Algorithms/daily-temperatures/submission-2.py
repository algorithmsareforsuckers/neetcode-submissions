class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_tmp, prev_day = stack.pop()
                res[prev_day] = i - prev_day
            
            stack.append((temp, i))
        
        return res