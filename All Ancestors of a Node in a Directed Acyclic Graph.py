class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # build the graph opposite of what is shown
        ans = [[] for i in range(n)]
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[v].append(u)
        def dfs(at, visited, ans):
            if visited[at]:
                return
            visited[at] = True
            for to in graph[at]:
                if visited[to]: continue
                ans.append(to)
                dfs(to, visited,ans)


        for i in range(n):
            visited = [False] * n
            dfs(i, visited, ans[i])
        for i in range(n):
            ans[i].sort()

        return ans
