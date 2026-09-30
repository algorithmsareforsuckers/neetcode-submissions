class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        need_to_end_with = 0
        start, curr = 0,0
        for i in range(len(gas)):
            curr += gas[i] - cost[i]

            if curr < 0:
                need_to_end_with -= curr
                start = i+1
                curr = 0
        
        if need_to_end_with > curr:
            return -1
        return start