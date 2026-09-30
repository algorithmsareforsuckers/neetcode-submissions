class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        counts = defaultdict(int)
        pre = defaultdict(list)
        for i in range(numCourses):
            counts[i] = 0


        for course, prereq in prerequisites:
            counts[course] += 1
            pre[prereq].append(course)
        
        q = deque()
        for course, count in counts.items():
            if count == 0: q.append(course)
        
        while q:
            for i in range(len(q)):
                c = q.popleft()
                for course in pre[c]:
                    counts[course] -= 1
                    if counts[course] == 0: q.append(course)
        
        for course, count in counts.items():
            if count != 0: return False
        return True