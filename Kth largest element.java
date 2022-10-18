class Solution {
    public int findKthLargest(int[] nums, int k) {
        //since we want the largest element - k we can store just k element and the last element is the one
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i = 0; i < nums.length; i++){
            heap.offer(nums[i]);
            if(heap.size() > k)
                heap.poll();
        }
        return heap.poll();
    }
}
