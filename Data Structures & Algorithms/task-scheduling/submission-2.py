class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for t in tasks:
            counts[ord(t) - ord("A")] += 1

        counts.sort()
        max_f = counts[-1]

        num_max = 0
        while max_f == counts[-num_max - 1]:
            num_max += 1

        time = (max_f - 1) * (n+1) + num_max
        return max(time, len(tasks))