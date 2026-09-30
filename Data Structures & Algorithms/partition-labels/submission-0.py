class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        seen = {}


        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]][1] = i
            
            else:
                seen[s[i]] = [i,i]

        q = [s[0]]
        i = seen[q[0]][0]
        start = i
        stop = seen[q[0]][1]+1

        while i < len(s):
            if i == stop:
                # new substring
                res.append(stop - start)
                start = i
                stop = seen[s[i]][1]+1
            
            stop = max(stop, seen[s[i]][1]+1)
            i += 1
        
        res.append(stop - start)
        return res
