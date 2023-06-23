class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # same as https://cses.fi/problemset/task/1132
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(at, parent, depth, dist):
            dist[at] = depth
            for to in graph[at]:
                if to == parent:
                    continue
                dfs(to, at, depth + 1, dist)
        dist_one, dist_two = [0] * n, [0] * n
        dfs(0, 0, 0, dist_one)
        max_idx = dist_one.index(max(dist_one))
        dfs(max_idx, max_idx, 0, dist_one)
        max_idx = dist_one.index(max(dist_one))
        dfs(max_idx, max_idx, 0, dist_two)
        
        for i in range(n):
            dist_two[i] = max(dist_two[i], dist_one[i])
        min_ = min(dist_two)
        ans = []
        for idx, val in enumerate(dist_two):
            if val == min_:
                ans.append(idx)
        return ans
