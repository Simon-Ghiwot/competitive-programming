class Solution {
    public int maxArea(int[] heights) {
        int left = 0, right = heights.length - 1;
        int maxArea = 0;
        
        while(left < right){
            int base = right - left;
            int height = Math.min(heights[left], heights[right]);
            int currArea = base * height;
            
            maxArea = Math.max(maxArea, currArea);
            
            if(heights[left] < heights[right])
                left++;
            else
                right--;
        }
        return maxArea;
    }
}
