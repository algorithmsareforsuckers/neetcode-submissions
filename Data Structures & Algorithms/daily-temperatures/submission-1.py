class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        hist = []

        for i in range(len(temperatures)):
            while hist != [] and temperatures[i] > hist[-1][1]:
                res[hist[-1][0]] = i - hist[-1][0]
                hist.pop()
            
            hist.append((i, temperatures[i]))

        return res
