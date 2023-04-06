class Solution {
    private List<List<Integer>> result;
    public List<List<Integer>> subsets(int[] nums) {
        result = new ArrayList<>();
        backtracking(0, new ArrayList<>(), nums);
        return result;
    }
    private void backtracking(int start, List<Integer> current, int [] nums){
        result.add(new ArrayList<>(current));
        if(start >= nums.length)
            return;
        for(int i = start; i < nums.length; i++){
            current.add(nums[i]);
            backtracking(i + 1, current, nums);
            current.remove(current.size() - 1);
        }
    }
}
