// First time i didn't solve it on my own but then i did after a while
class Solution {
    private int SIZE = 9;
    private char EMPTY_SPACE = '.';
    public void solveSudoku(char[][] board) {
        backtrack(board, 0);
    }
    private boolean backtrack(char[][] board, int combined){
        int row = combined / SIZE;
        int col = combined % SIZE;

        if(combined > 80)   return true;

        if(board[row][col] == EMPTY_SPACE){
            for(char current = '1'; current <= '9'; current++){
                if(!isValid(row, col, board, current))  continue;
                board[row][col] = current;
                if(backtrack(board, combined + 1))
                    return true;
                board[row][col] = EMPTY_SPACE;
            }
            return false;
        }
        else
            return backtrack(board, combined + 1);
    }
    private boolean isValid(int row, int col, char[][] board, char current){
        int blockRow = (row / 3) * 3, blockCol = (col / 3) * 3; // to get the correct block
        for(int i = 0; i < 9; i++){
            if(board[row][i] == current || board[i][col] == current)    return false;
            if(board[blockRow + i / 3][blockCol + i % 3] == current)    return false;
        }
        return true;
    }
}
