class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        return backtracking(nums, 0, target, 0);
    }
    private int backtracking(int [] nums, int total, int target, int index){
        if(index == nums.length && target == total)
            return 1;
        if(index == nums.length)
            return 0;
        return backtracking(nums, total + nums[index], target, index + 1) + 
               backtracking(nums, total - nums[index], target, index + 1);
    }
}
// brute force
// how to approach dp
    // 1. find type of question can be knapsack, lcs, lis, fibinacci
    // 2. base case
    // 3. decision space
    // 4. find brute force
    // 5. optimize to memo
    // 6. optimize to tabulation
