class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = [[] for _ in range(len(accounts))]

        for i in range(len(accounts)):
            name, emails = accounts[i][0], set(accounts[i][1:])

            for j in range(i+1, len(accounts)):
                Name, Emails = accounts[j][0], set(accounts[j][1:])
                if Name == name:
                    if len(emails.intersection(Emails)) > 0:
                        graph[i].append(j)
                        graph[j].append(i)
        
        visited = set()
        res = []
        def dfs(current, visited, emails):
            if current in visited:
                return 
            
            visited.add(current)
            for i in accounts[current][1:]:
                emails.add(i)
            for child in graph[current]:
                dfs(child, visited, emails)
                
        for i in range(len(accounts)):
            if i not in visited:
                emails = set()
                name = accounts[i][0]
                dfs(i, visited, emails)
                Sorted = sorted(list(emails))
                res.append([name, *Sorted])
        return res
