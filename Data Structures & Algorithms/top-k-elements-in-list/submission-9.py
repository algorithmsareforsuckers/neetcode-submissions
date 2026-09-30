class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [] # ith index stores all numbers which are present i-1 times (list is 0indexed)

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            buckets.append([])
        
        for key, value in counts.items():
            buckets[value - 1] = buckets[value - 1] + [key]
        
        res = []
        for numbers in reversed(buckets):
            print(numbers)
            res = res + numbers
            if len(res) == k:
                return res
        return -1
