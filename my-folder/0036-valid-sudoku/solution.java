class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> rows = null;
        Set<Character> cols = null;
        Set<Character> blocks = null;

        for(int i = 0; i<9; i++){
            rows = new HashSet<Character>();
            cols = new HashSet<Character>();
            blocks = new HashSet<>();

            int row = 3 * (i/3);
            int col = 3 * (i%3);
            
            for(int j=0;j<9;j++) {
                if(board[i][j] != '.' && !rows.add(board[i][j])) return false;
                if(board[j][i] != '.' && !cols.add(board[j][i])) return false;
                if(board[row + j/3][col + j%3] != '.' && !blocks.add(board[row + j/3][col + j%3])) return false;
            }
        }

        return true;
    }
}
