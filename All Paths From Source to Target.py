class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = [False] * len(graph)
        def dfs(visited, at, path, ans, target):
            path.append(at)
            if at == target:
                ans.append(path[:])
            if visited[at]:
                return
            visited[at] = True
            for to in graph[at]:
                dfs(visited, to, path, ans, target)
            visited[at] = False
            path.pop()
        
        ans = []
        dfs(visited, 0, [], ans, len(visited) - 1)
        return ans
