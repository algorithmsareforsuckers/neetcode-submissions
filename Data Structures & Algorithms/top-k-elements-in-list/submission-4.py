class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my new thought is just make the counts hashmap, then get a list where items are list [key, value], then sort with key being value
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        fin = []
        for key, val in counts.items():
            fin.append([key, val])
        
        fin.sort(key=lambda x: -x[1])

        res = []
        for pair in fin[0:k]:
            res.append(pair[0])

        return res
