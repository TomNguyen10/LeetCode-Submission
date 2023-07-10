class Solution {
    public void rotate(int[][] matrix) {
        for (int r = 0; r < matrix.length; r++) {
            for (int c = r; c < matrix[0].length; c++) {
                int temp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = temp;
            }
        }

        for (int r = 0; r < matrix.length; r++) {
            for (int c = 0; c < matrix.length/2; c++) {
                int temp = matrix[r][c];
                matrix[r][c] = matrix[r][matrix.length - 1 - c];
                matrix[r][matrix.length - 1 - c] = temp;
            }
        }
    }
}
