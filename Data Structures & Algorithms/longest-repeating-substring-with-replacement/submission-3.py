import heapq as hq
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # can change k chars, need max substring no repeats.

        # outline of idea: build out sliding window, update l pointer when would require k+1 updates to have no repeats. 
        # Keep track of the longest the window has been

        best = 0
        unique = []
        for c in s:
            if c not in unique:
                unique.append(c)

        for c in unique:
            l = 0
            wrong = []
            # for each unique character, ignore it and see if it is the best option
            print(c)
            for r in range(len(s)):
                if s[r] == c:
                    if r-l+1 > best:
                        best = r-l+1
                    continue

                if k == 0:
                    l = r+1
                elif wrong == []:
                    hq.heappush(wrong, r) 
                else:
                    if len(wrong) >= k:
                        l = max(l, wrong[0] + 1)
                        hq.heappop(wrong)
                    hq.heappush(wrong, r)

                if r - l + 1 > best:
                    best = r-l + 1
        return best






