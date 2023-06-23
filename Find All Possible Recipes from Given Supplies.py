class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        def dfs(at, visited, status):
            if at in visited:
                return status[at]
            visited.add(at)
            if len(edges[at]) == 0:
                status[at] = at in look_up
                return status[at]
            
            for to in edges[at]:
                status[to] = dfs(to, visited, status)
                if not status[to]:
                    return False
            return True

        edges, look_up = defaultdict(list), set(supplies)
        for i in range(len(recipes)):
            edges[recipes[i]] = ingredients[i]
        ans = []
        visited, status = set(), defaultdict(bool)
        for i in range(len(recipes)):
            if recipes[i] in visited:
                if status[recipes[i]]:
                    ans.append(recipes[i])
                continue
            status[recipes[i]] = dfs(recipes[i], visited, status)
            if status[recipes[i]]:
                ans.append(recipes[i])
        
        return ans
