class Solution {
    public int maxSum(int[][] grid) {
        int [][] prefix = new int [grid.length][grid[0].length + 1];
        for(int i = 0; i < grid.length; i++)
            for(int j = 0; j < grid[0].length; j++)
                prefix[i][j + 1] = prefix[i][j] + grid[i][j];
        int result = 0;
        for(int i = 2; i < grid.length; i++)
            for(int j = 3; j < prefix[0].length; j++){
                int top = prefix[i - 2][j] - prefix[i - 2][j - 3];
                int middle = prefix[i - 1][j - 1] - prefix[i - 1][j - 2];
                int bottom = prefix[i][j] - prefix[i][j - 3];
                result = Math.max(result, top + middle + bottom);
            }

        return result;
    }
}
