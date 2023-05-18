class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 0
        
        def dfs(edges, at, visited):
            if visited[at]:
                return 0
            total = 1
            visited[at] = True
            for to in edges[at]:
                if visited[to]:
                    continue
                total += dfs(edges, to, visited)
            return total


        edges = [[] for i in range(len(bombs))]
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                distance = sqrt(pow(bombs[j][0] - bombs[i][0], 2) + pow(bombs[j][1] - bombs[i][1], 2))
                if distance <= bombs[i][2]:
                    edges[i].append(j)

        for i in range(len(bombs)):
            visited = [False] * len(bombs)
            ans = max(ans, dfs(edges, i, visited))

        return ans
