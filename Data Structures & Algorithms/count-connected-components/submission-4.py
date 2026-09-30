class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        array = defaultdict(list)

        for v,w in edges:
            array[v].append(w)
            array[w].append(v)
            
        visited = set()

        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                q = deque([i])

                while q:
                    curr = q.popleft()
                    for neighbor in array[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
        return res


