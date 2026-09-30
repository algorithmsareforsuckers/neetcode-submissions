class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # so having nums[i] + nums[j] + nums[k] = 0 is true iff nums[i] + nums[j] = -nums[k]. 
        # So, we can iterate on k, and we only have to check the pairs to the left of k
        # computing every pair for every k would still be very expensive, we need a better way.
        # first thing I think of is to maintain a heap with sums which have been seen as keys, and values are the 2 indexes.
        # This is space inefficient? It's storing up to 1000 choose 2 values, which is too many, I think.

        # Also anytime we see a triple which works, we need to make sure we never add an equivalent triple. We can maintain a "barred" list.


        # for O(n^2) we can have for every k, then loop twice, storing 1 value for each j which would make (nums[k],nums[j],val) work.

        # another view is we are solving 2 sum for target -nums[k].
        # maybe: sort list first
        mono = sorted(nums)

        solves = []
        for k in range(len(mono)):
            # solve 2-sum with target k in O(n) -- results in O(n^2) total time.
            l = 0
            r = len(mono) - 1
            while l < r:
                if l == k or mono[l] + mono[r] < -mono[k]:
                    l += 1
                elif r == k or mono[l] + mono[r] > -mono[k]:
                    r -= 1
                else:
                    possible = sorted([mono[l], mono[r], mono[k]])
                    if possible not in solves:
                        solves.append(possible)
                    l += 1
        
        return solves