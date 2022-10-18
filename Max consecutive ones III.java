class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, right = 0; 
        int count = 0, max = 0;
        while(right < nums.length){
            if(nums[right] == 1)
                count++;
            while(count + k < right - left + 1){
                if(nums[left++] == 1)
                    count--;
            }
            max = Math.max(max, right - left + 1);
            right++;
        }
        return max;
    }
}
//i can move my left while count + K is less than my window
