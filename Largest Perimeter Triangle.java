class Solution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        int result = 0;
        for(int i = 0; i < nums.length - 2; i++){
            if(isValidTraingle(new int[] {nums[i], nums[i + 1], nums[i + 2]}))
                result = Math.max(result, nums[i] + nums[i + 1] + nums[i + 2]);
        }
        return result;
    }
    boolean isValidTraingle(int [] sides){
        return sides[0] + sides[1] > sides[2] && 
                sides[2] + sides[1] > sides[0] &&
                sides[0]+ sides[2] > sides[1]; 
    }
}
