class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        def dfs(board, x, y):
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board) or board[y][x] != 'O':
                return
            board[y][x] = '#'
            dfs(board, x + 1, y)
            dfs(board, x - 1, y)
            dfs(board, x, y - 1)
            dfs(board, x, y + 1)
        
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(board, 0, r)
            if board[r][cols - 1] == 'O':
                dfs(board, cols - 1, r)
        
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(board, c, 0)
            if board[rows - 1][c] == 'O':
                dfs(board, c, rows - 1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'

