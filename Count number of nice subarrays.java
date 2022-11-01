class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
         for(int i = 0; i < nums.length; i++)
            nums[i] = (nums[i] % 2 == 0 ? 0 : 1);
        int result = 0, sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            if(map.containsKey(sum - k))
                result += map.get(sum - k);//get how many sub arrays we can generate that has a prefix of sum - k
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return result;
    }
}
