class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the maximum possible multiplicity for an individual number is |nums| - (k-1). Want to store nums with 0 -> that count
        mults = [[] for _ in range(len(nums) - (k-1))] # will store list of nums with index count - 1
        counts = defaultdict(int) # each number to its count

        for num in nums:
            counts[num] += 1 # could also just use Counter() from collections

        for key, value in counts.items():
            mults[value-1].append(key)
        
        res = []
        for vals in reversed(mults):
            res = res + vals
            if len(res) >= k:
                return res
        
        return res
        
