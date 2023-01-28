class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        Arrays.sort(nums);

        int startIndex = binarySearch(nums, target, true);
        int endIndex = binarySearch(nums, target, false);
        List<Integer> result = new ArrayList<>();
        if(startIndex != -1)
            for(int i = startIndex; i < endIndex + 1; i++)
                result.add(i);

        return result;
    }
    public int binarySearch(int []nums, int target, boolean first){
        int left = 0, right = nums.length - 1, index = -1;
        
        while(left <= right){
            
            int mid = left + (right - left)/2;
            if(target == nums[mid]){
                index = mid;
                if(first)
                    right = mid - 1;
                else
                    left = mid + 1;
            }
            else if(nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return index;
    }
}
