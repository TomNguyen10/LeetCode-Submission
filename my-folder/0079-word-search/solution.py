class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(matrix, current, target, row, col, visited):
            if current == target:
                return True
            
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or visited[row][col] or matrix[row][col] != target[len(current)]:
                return False
            
            visited[row][col] = True

            found = backtrack(matrix, current + matrix[row][col], target, row+1, col, visited) or backtrack(matrix, current + matrix[row][col], target, row-1, col, visited) or backtrack(matrix, current + matrix[row][col], target, row, col+1, visited) or backtrack(matrix, current + matrix[row][col], target, row, col-1, visited)

            visited[row][col] = False

            return found
        
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(board, "", word, i, j, visited):
                    return True

        return False
