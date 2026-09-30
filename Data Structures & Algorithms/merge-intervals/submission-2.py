class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        mono = sorted(intervals)
        print(mono)
        res_hash = {1 : mono[0]}
        int_num = 1

        for j in range(len(mono) - 1):
            if res_hash[int_num][1] >= mono[j+1][0]:
                res_hash[int_num][1] = max(mono[j+1][1], res_hash[int_num][1])
            else:
                int_num += 1
                res_hash[int_num] = mono[j+1]
        
        return list(res_hash.values())
