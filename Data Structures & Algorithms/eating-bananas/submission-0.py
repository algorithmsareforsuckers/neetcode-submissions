class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mono = sorted(piles) # O(|piles|log(|piles|)

        r = mono[-1] #max possible num bananas needed
        l = 1
        mi = mono[-1]

        while l <= r:
            mid = l + (r-l)//2

            # check if feasible
            hrs = 0
            for p in piles:
                if p%mid == 0:
                    hrs += p//mid
                else:
                    hrs += p//mid + 1
            
            if hrs <= h:
                # worked, so update mi, check smaller
                mi = min(mi, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return mi

