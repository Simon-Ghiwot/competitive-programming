class Solution {
    public int orangesRotting(int[][] grid) {
        int time = -1, current = 0, initialFresh = 0;       
        Queue<Integer> rottingRow = new LinkedList<>();
        Queue<Integer> rottingCol = new LinkedList<>();
        int [][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for(int i = 0; i < grid.length; i++)
            for(int j = 0; j < grid[0].length; j++)
                if(grid[i][j] == 2){
                    rottingRow.add(i);
                    rottingCol.add(j);
                }
                else if (grid[i][j] == 1)
                    initialFresh++;
        
        while(!rottingRow.isEmpty())
        {
            current = rottingRow.size();
            for(int i = 0; i < current; i++){
                int row = rottingRow.remove();
                int col = rottingCol.remove();

                for(int [] d : dir){
                    int r = row + d[0], c = col + d[1];
                    if(!is_valid(grid, r, c))   continue;
                    grid[r][c] = 2;
                    rottingRow.add(r);   rottingCol.add(c);
                }
            }
            time++;
        }
        for(int i = 0; i < grid.length; i++)
            for(int j = 0; j < grid[0].length; j++)
                if(grid[i][j] == 1 && initialFresh > 0)
                    return -1;
                else if (initialFresh == 0)
                    return 0;
        return time;
    }
    boolean is_valid(int [][]grid, int row, int col){
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] != 1)
            return false;
        return true;
    }
}
