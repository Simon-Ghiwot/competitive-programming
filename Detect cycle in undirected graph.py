class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
    #Code here
		visited = [False] * len(adj)
                def dfs(at, parent, visited):
                      if visited[at]:
                           return True
                      visited[at] = True
                      for to in adj[at]:
                           if to == parent:
                                continue
                           if dfs(to, at, visited):
                                return True
                       return False
                 for i in range(len(adj)):
                       if visited[i]: continue
                       if dfs(i, i, visited):
                             return True
                 return False
