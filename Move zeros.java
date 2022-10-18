class Solution {
    public void moveZeroes(int[] nums) {
        if(nums == null || nums.length == 0)
            return;
        int pivot = 0;//points to the first zero digit
        for(int i = 0; i < nums.length; i++)
            if(nums[i] == 0){
                pivot = i;
                break;
            }
        for(int i = pivot; i < nums.length && pivot < nums.length; i++){
            if(nums[i] != 0){
                int temp = nums[pivot];
                nums[pivot] = nums[i];
                nums[i] = temp;
                pivot++;
            }
        }
    }
}
