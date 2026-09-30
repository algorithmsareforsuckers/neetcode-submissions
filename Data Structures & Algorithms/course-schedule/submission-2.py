class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course] += 1
            adj[prereq].append(course)
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0
        while q:
            prereq = q.popleft()
            taken += 1
            for course in adj[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return taken == numCourses 
                