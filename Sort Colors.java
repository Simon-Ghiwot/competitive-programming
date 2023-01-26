class Solution {
    public void sortColors(int[] nums) {
        int left = 0, right = nums.length - 1;
        for(int i = 0; i <= right; ){
            if(nums[i] == 0)
                swap(nums, i, left++);
            else if(nums[i] == 2){
                swap(nums, i, right--);
                continue;
            }            
            i++;
        }
    }
    private void swap(int [] nums, int first, int second){
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }
}


