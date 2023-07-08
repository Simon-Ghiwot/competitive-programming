class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        edges = [[] for i in range(len(s))]
        ans = [x for x in s]
        visited = [False] * len(s)
        def dfs(at, visited, components, letters):
            if visited[at]:
                return
            visited[at] = True
            components.append(at)
            letters.append(s[at])
            for to in edges[at]:
                dfs(to, visited, components, letters)
            
        for u, v in pairs:
            edges[u].append(v)
            edges[v].append(u)
        
        for i in range(len(s)):
            if visited[i]: continue
            components , letters = [], []
            dfs(i, visited, components, letters)
            components.sort()
            letters.sort()
            for j in range(len(letters)):
                ans[components[j]] = letters[j]
        return "".join(ans)
