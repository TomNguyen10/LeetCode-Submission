class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        pacific_reachable = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic_reachable = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r, c, reachable, prev_height):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                reachable[r][c] or heights[r][c] < prev_height):
                return
            reachable[r][c] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, reachable, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pacific_reachable, heights[r][0])
            dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pacific_reachable, heights[0][c])
            dfs(rows - 1, c, atlantic_reachable, heights[rows - 1][c])
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])
        
        return result
