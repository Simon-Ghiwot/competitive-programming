class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length, col = matrix[0].length;
        int right = 0, left = row * col - 1;
        
        while(right <= left){
            int mid = (right + left)/2;
            if(matrix[mid / col][mid % col] == target)
                return true;
            else if(matrix[mid / col][mid % col] > target)
                left = mid - 1;
            else
                right = mid + 1;
        }
        
         return false;   
    }
}
