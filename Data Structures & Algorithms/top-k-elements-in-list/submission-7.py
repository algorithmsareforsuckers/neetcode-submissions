from collections import Counter
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for key, val in counts.items():
            buckets[val].append(key)
        
        res = []
        for entries in reversed(buckets):
            print(entries)
            res += entries
            if len(res) >= k:
                return res[:k]
        return res
