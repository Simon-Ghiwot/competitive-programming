class Solution {
    public boolean isValidSudoku(char[][] board) {
        int length = 9;
        for(int i = 0; i < length; i++){
            Set<Character> seen = new HashSet<>();
            for(int j = 0; j < length; j++){
                if(board[i][j] == '.')  continue;
                if(seen.contains(board[i][j]))  return false;
                seen.add(board[i][j]);
            }
        }
        for(int i = 0; i < length; i++){
            Set<Character> seen = new HashSet<>();
            for(int j = 0; j < length; j++){
                if(board[j][i] == '.')  continue;
                if(seen.contains(board[j][i]))  return false;
                seen.add(board[j][i]);
            }
        }
        for(int i = 0; i < length; i += 3){ 
            for(int j = 0; j < length; j += 3){
                Set<Character> seen = new HashSet<>();
                if(!isBoxValid(board, i, j, seen))
                    return false;
            }
        }
        return true;
    }
    private boolean isBoxValid(char [][] board, int row, int col, Set<Character> seen){
        for(int i = row; i < row + 3; i++){
            for(int j = col; j < col + 3; j++){
                if(board[i][j] == '.')  continue;
                if(seen.contains(board[i][j]))  return false;
                seen.add(board[i][j]);
            }
        }
        return true;
    }
}
