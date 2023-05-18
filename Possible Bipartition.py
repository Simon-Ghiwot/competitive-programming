class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        edges = [[] for i in range(n)]
        for u, v in dislikes:
            edges[u - 1].append(v - 1)
            edges[v - 1].append(u - 1)
        color = [False] * n
        visited = [False] * n
        que = deque()
        for i in range(n):
            if visited[i]:
                continue
            que.append(i)
            while que:
                at = que.popleft()
                for to in edges[at]:
                    if visited[to]:
                        if color[at] == color[to]:
                            return False
                    else:
                        visited[to] = True
                        color[to] = color[at] ^ 1
                        que.append(to)
        return True
