import heapq
class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []


    def addNum(self, num: int) -> None:
        if not self.small: 
            heapq.heappush(self.small, -num)
            return

        if num > -self.small[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.large) > len(self.small)+1:
            min_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -min_large)
        elif len(self.small) > len(self.large)+1:
            max_small = heapq.heappop(self.small)
            heapq.heappush(self.large, -max_small)
        
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            max_small = -self.small[0]
            min_large = self.large[0]
            return (max_small + min_large) / 2
        
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        return self.large[0]
        
        