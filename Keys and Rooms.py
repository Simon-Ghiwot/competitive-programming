class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(visited, at):
            if at in visited:
                return
            visited.add(at)
            for to in rooms[at]:
                dfs(visited, to)
        visited = set()
        dfs(visited, 0)
        return len(visited) == len(rooms)
