class Solution {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for(int num : nums) total += num;
        if(total % 2 != 0)  return false;
        int target = total / 2;
        boolean [][] dp = new boolean [nums.length + 1][target + 1];
        for(int i = 0; i <= nums.length; i++)
            for(int j = 0; j <= target; j++){
                if(i == 0 || j == 0){
                    if(i == 0)  dp[i][j] = false;
                    else dp[i][j] = true;
                }
                else if(j < nums[i - 1])
                    dp[i][j] = dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
            }
        return dp[nums.length][target];
    }
}
//find a subset sum that sums to total / 2 if so return true else return false 
// basic knapsack dp varation
