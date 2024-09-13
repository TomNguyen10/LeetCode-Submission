class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(matrix, current, target, row, col, visited):
            if current == target:
                return True
            
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or visited[row][col] or matrix[row][col] != target[len(current)]:
                return False
            
            visited[row][col] = True

            up = backtrack(matrix, current + matrix[row][col], target, row + 1, col, visited)
            down = backtrack(matrix, current + matrix[row][col], target, row - 1, col, visited)
            right = backtrack(matrix, current + matrix[row][col], target, row, col + 1, visited)
            left = backtrack(matrix, current + matrix[row][col], target, row, col - 1, visited)

            found = up or down or right or left

            visited[row][col] = False

            return found
        
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                res = backtrack(board, "", word, r, c, visited)
                if res:
                    return True
        
        return False
