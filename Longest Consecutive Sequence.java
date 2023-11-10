class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for(int i = 0; i < nums.length; i++)
            seen.add(nums[i]);
        int max = 0;
        for(int i = 0; i < nums.length; i++){
            if(seen.contains(nums[i] - 1))
                continue;
            int localMax = 1;
            while(seen.contains(nums[i] + localMax)){
                localMax++;
            }
            max = Math.max(max, localMax);
        }
        return max;
    }
}
