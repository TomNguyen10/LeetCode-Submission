class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'R':
                    # Check north
                    for n in range(r - 1, -1, -1):
                        if board[n][c] == 'p':
                            res += 1
                            break
                        if board[n][c] == 'B':
                            break
                    # Check south
                    for s in range(r + 1, len(board)):
                        if board[s][c] == 'p':
                            res += 1
                            break
                        if board[s][c] == 'B':
                            break
                    # Check west
                    for w in range(c - 1, -1, -1):
                        if board[r][w] == 'p':
                            res += 1
                            break
                        if board[r][w] == 'B':
                            break
                    # Check east
                    for e in range(c + 1, len(board[0])):
                        if board[r][e] == 'p':
                            res += 1
                            break
                        if board[r][e] == 'B':
                            break
                    return res

