class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)

        heap = [(-value, key) for key, value in counts.items()]
        heapq.heapify(heap)

        cooldown = collections.deque([])
        time = 0

        while heap or cooldown:
            print(cooldown)
            if cooldown and cooldown[-1][0] <= time:
                _, v, k = cooldown.pop()
                heapq.heappush(heap, (v,k))
            
            if heap:
                val, key = heapq.heappop(heap)
                val += 1
                
                if val < 0:
                    cooldown.appendleft((time + n + 1, val, key))
                    
            time += 1
        
        return time
            
