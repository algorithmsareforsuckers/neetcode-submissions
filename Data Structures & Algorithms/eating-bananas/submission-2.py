class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mi = max(piles)

        r = mi #max possible num bananas needed
        l = 1

        while l <= r:
            mid = l + (r-l)//2

            # check if feasible
            hrs = 0
            for p in piles:
                hrs += (p + mid - 1) // mid
            if hrs <= h:
                # worked, so update mi, check smaller
                mi = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return mi
