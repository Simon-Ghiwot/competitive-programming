class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        min_ = 1e10
        def dfs(at, visited):
            if visited[at]:
                return 
            nonlocal min_
            visited[at] = True
            for to, weight in edges[at]:
                min_ = min(min_, weight)
                dfs(to, visited)
        
        visited = [False] * (n + 1)
        edges = defaultdict(list)
        for u, v, w in roads:
            edges[u].append((v, w))
            edges[v].append((u, w))
        dfs(1, visited)
        return min_
