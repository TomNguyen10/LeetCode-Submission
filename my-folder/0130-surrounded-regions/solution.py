class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, row, col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'O':
                return
            board[row][col] = '#'
            dfs(board, row - 1, col)
            dfs(board, row + 1, col)
            dfs(board, row, col - 1)
            dfs(board, row, col + 1)

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(board, r, 0)
            if board[r][cols - 1] == 'O':
                dfs(board, r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(board, 0, c)
            if board[rows - 1][c] == 'O':
                dfs(board, rows - 1, c)
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
