class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        cr, cc = click
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
            return board
        
        def dfs(board, row, col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'E':
                return

            moves = [[row-1, col-1], [row-1, col], [row-1, col+1], 
                     [row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]
            
            mine_count = 0
            for move in moves:
                if 0 <= move[0] < len(board) and 0 <= move[1] < len(board[0]) and board[move[0]][move[1]] == 'M':
                    mine_count += 1
            
            if mine_count > 0:
                board[row][col] = str(mine_count)
            else:
                board[row][col] = 'B'
                for move in moves:
                    dfs(board, move[0], move[1])
        
        dfs(board, cr, cc)

        return board

