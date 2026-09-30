class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0]*numCourses
        pre = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course] += 1
            pre[prereq].append(course)
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        while q:
            prereq = q.popleft()
            res.append(prereq)
            taken += 1

            for course in pre[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        if taken != numCourses:
            return []
        return res
