class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        edges = [[] for i in quiet]
        ans = [0] * len(quiet)
        visited = [False] * len(quiet)

        def dfs(at, visited, ans):
            if visited[at]:
                return ans[at]
            visited[at] = True
            ans[at] = at
            for to in edges[at]:
                res = dfs(to, visited, ans)
                if quiet[res] < quiet[ans[at]]:
                    ans[at] = res
            return ans[at]
        for u, v in richer:
            edges[v].append(u)

        for i in range(len(quiet)):
            if not visited[i]:
                ans[i] = dfs(i, visited, ans)

        return ans
