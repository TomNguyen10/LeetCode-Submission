class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, row, col, oriCol, color):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != oriCol:
                return
            image[row][col] = color
            dfs(image, row - 1, col, oriCol, color)
            dfs(image, row + 1, col, oriCol, color)
            dfs(image, row, col - 1, oriCol, color)
            dfs(image, row, col + 1, oriCol, color)

        originalColor = image[sr][sc]
        if originalColor != color:
            dfs(image, sr, sc, originalColor, color)
        
        return image

