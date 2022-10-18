class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0, right = 0, max = 0;
        long total = 0;
        while(right < nums.length){
            total += nums[right];
            while((right - left + 1) * (long) nums[right] > total + k)
                total -= nums[left++];
                
            max = Math.max(max, right - left + 1);
            right++;
        }
        return max;
    }
}
