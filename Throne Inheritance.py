class ThroneInheritance:

    def __init__(self, kingName: str):
        self.status = defaultdict(int)
        self.edges = defaultdict(list)
        self.edges[kingName]
        self.king = kingName
        self.status[self.king] = True

    def birth(self, parentName: str, childName: str) -> None:
        self.edges[parentName].append(childName)
        self.status[childName] = True

    def death(self, name: str) -> None:
        self.status[name] = False

    def getInheritanceOrder(self) -> List[str]:
        def dfs(path, at):
            if self.status[at] == True:
                path.append(at)
            for to in self.edges[at]:
                dfs(path, to)
            
        path = []
        dfs(path, self.king)
        return path


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
