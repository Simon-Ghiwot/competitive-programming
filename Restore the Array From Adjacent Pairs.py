class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        indgree = defaultdict(int)
        for u, v in adjacentPairs:
            edges[u].append(v)
            edges[v].append(u)
            indgree[u] += 1
            indgree[v] += 1
        que, ans = deque(), []
        for key in indgree.keys():
            if indgree[key] == 1:
                que.append(key)
                break
        while que:
            at = que.popleft()
            ans.append(at)
            for to in edges[at]:
                indgree[to] -= 1
                if indgree[to] == 1:
                    que.append(to)
        look_up = set(ans)
        for key in indgree.keys():
            if indgree[key] == 0 and key not in look_up:
                ans.append(key)
        return ans
