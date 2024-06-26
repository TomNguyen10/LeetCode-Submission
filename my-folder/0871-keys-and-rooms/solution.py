class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        def dfs(rooms, current, visited):
            for key in rooms[current]:
                if not visited[key]:
                    visited[key] = True
                    dfs(rooms, key, visited)
        
        dfs(rooms, 0, visited)

        for visit in visited:
            if not visit: return False
        
        return True
