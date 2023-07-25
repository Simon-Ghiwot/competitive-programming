class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        edges = defaultdict(list)
        for u, v in stones:
            edges[(u, "*")].append((u, v))
            edges[("*", v)].append((u, v))
        visited, ans = set(), 0
    
        for u, v in stones:
            if (u, v) in visited:
                continue
            que, cur = deque(), 0
            que.append((u, v))
            visited.add((u, v))
            while que:
                r, c = que.popleft()
                cur += 1
                patterns = [(r, "*"), ("*", c)]
                for pattern in patterns:
                    for to in edges[pattern]:
                        if to not in visited:
                            visited.add(to)
                            que.append(to)
            ans += cur - 1
        return  ans 
        
