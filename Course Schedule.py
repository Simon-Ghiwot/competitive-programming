class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for i in range(numCourses)]
        indgree = [0] * numCourses
        for u, v in prerequisites:
            edges[u].append(v)
            indgree[v] += 1
        que, cnt = deque(), 0
        for i in range(numCourses):
            if indgree[i] == 0:
                que.append(i)
        while que:
            at = que.pop()
            cnt += 1
            for to in edges[at]:
                indgree[to] -= 1
                if indgree[to] == 0:
                    que.append(to)

        return cnt == numCourses
