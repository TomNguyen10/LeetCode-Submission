class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        traversed = []

        step = 1
        direction = 0
        while len(traversed) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if (
                        rStart >= 0
                        and rStart < rows
                        and cStart >= 0
                        and cStart < cols
                    ):
                        traversed.append([rStart, cStart])
                    rStart += dir[direction][0]
                    cStart += dir[direction][1]

                direction = (direction + 1) % 4
            step += 1
        return traversed
