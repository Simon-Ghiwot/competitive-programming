class Solution {
    public void rotate(int[] nums, int k) {
        if(k == 0 || k % nums.length == 0)
            return;
        k = k % nums.length;
        int [] temp = new int [k];
        int [] temp2 =  new int [nums.length - k];
        int left = 0;
        for(int i = nums.length - k; i < nums.length; i++)
            temp[left++] = nums[i];
        for(int i = 0; i < nums.length - k; i++)
            temp2[i] = nums[i];
        for(int i = 0; i < temp.length;i++)
            nums[i] = temp[i];
        for(int i = k; i < nums.length; i++)
            nums[i] = temp2[i-k] ;

    }
}
