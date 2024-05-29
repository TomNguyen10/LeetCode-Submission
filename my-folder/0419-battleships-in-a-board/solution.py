class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(board, x, y):
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board) or board[y][x] == '.':
                return 
            board[y][x] = '.'
            dfs(board, x - 1, y)
            dfs(board, x + 1, y)
            dfs(board, x, y - 1)
            dfs(board, x, y + 1)

        res = 0

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    res += 1
                    dfs(board, c, r) 
        
        return res
