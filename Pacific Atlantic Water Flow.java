class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
                
        List<List<Integer>> result = new ArrayList<>();
        int row = heights.length, col = heights[0].length;
        boolean [][] visitedPacific = new boolean[row][col];
        boolean [][] visitedAtlantic = new boolean[row][col];
        
        for(int i = 0; i < col; i++)
        {   
            dfs(0, i, heights, visitedPacific, heights[0][i]);
            dfs(row - 1, i, heights, visitedAtlantic, heights[row - 1][i]);
        }
        
        for(int i = 0; i < row; i++)
        {
            dfs(i, 0, heights, visitedPacific, heights[i][0]);
            dfs(i, col - 1, heights, visitedAtlantic, heights[i][col - 1]);
        }
        
        
        for(int i = 0; i < row; i++)
            for(int j = 0; j < col; j++)
                if(visitedPacific[i][j] && visitedAtlantic[i][j])
                    result.add(Arrays.asList(i,j));
                
        return result;
    }
    public void dfs(int row, int col, int[][] heights, boolean [][] visited, int previous)
    {
        if(row < 0 || col < 0 || row >= heights.length || col >= heights[0].length || visited[row][col])
            return;
        if(heights[row][col] < previous)
            return;
         
        visited[row][col] = true;
        
        dfs(row - 1, col, heights, visited, heights[row][col]);
        dfs(row + 1, col, heights, visited, heights[row][col]);
        dfs(row, col - 1, heights, visited, heights[row][col]);
        dfs(row, col + 1, heights, visited, heights[row][col]);
    }
}
