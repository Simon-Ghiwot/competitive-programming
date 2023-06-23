class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        visited = [False] * len(graph)
        status = [False] * len(graph)
        def dfs(at, visited, ans):
            if visited[at]:
                return status[at]
            visited[at] = True
            res = True
            for to in graph[at]:
                res &= dfs(to, visited, ans)
            if res:
                ans.append(at)
            status[at] = res
            return status[at]

        for i in range(len(graph)):
            if visited[i]:  continue
            dfs(i, visited, ans)

        return sorted(ans)
