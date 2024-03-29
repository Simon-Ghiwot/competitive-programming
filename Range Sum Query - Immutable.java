class NumArray {
    private int[] nums;
    private int [] prefix;
    public NumArray(int[] nums) {
       this.nums = nums;
        prefix = new int[nums.length + 1];
        for(int i = 1; i <= nums.length; i++)
            prefix[i] = prefix[i - 1] + nums[i - 1]; 
    }
    
    public int sumRange(int left, int right) {
        return prefix[right + 1] - prefix[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */
