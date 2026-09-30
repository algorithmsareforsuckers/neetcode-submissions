class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.lar = nums
        heapq.heapify(self.lar)
        print(self.lar)
        
        for i in range(len(nums)-k):
            heapq.heappop(self.lar)

        print(self.lar)

    def add(self, val: int) -> int:
        if not self.lar or len(self.lar)<self.k:
            heapq.heappush(self.lar, val)
        elif (val > self.lar[0]):
            heapq.heappop(self.lar)
            heapq.heappush(self.lar, val)
        
        return self.lar[0]

        
