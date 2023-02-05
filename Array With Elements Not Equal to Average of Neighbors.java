class Solution {
    public int[] rearrangeArray(int[] nums) {
        Arrays.sort(nums);
        int [] result = new int[nums.length];

        int left = 0, right = nums.length - 1, i = 0;
        while(left < right){
            result[i] = nums[left++];
            result[i + 1] = nums[right--];
            i += 2;
        }
        if(nums.length % 2 == 1)
            result[nums.length - 1] = nums[left];
        return result;
    }
}
