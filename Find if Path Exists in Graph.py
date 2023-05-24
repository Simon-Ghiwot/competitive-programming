class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for i in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        visited = [False] * n
        que = deque()
        que.append(source)
        visited[source] = True
        while que:
            at = que.popleft()
            if at == destination:
                return True
            for to in g[at]:
                if visited[to]:
                    continue
                visited[at] = True
                que.append(to)
        return False
