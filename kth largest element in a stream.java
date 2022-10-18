class KthLargest {
    private int size;
    private PriorityQueue<Integer> heap;
    public KthLargest(int k, int[] nums) {
        size = k;
        heap = new PriorityQueue<>();
        for(int i = 0; i < nums.length; i++){
            heap.offer(nums[i]);
            if(heap.size() > size)
                heap.poll();
        }
    }
    
    public int add(int val) {
        heap.offer(val);
        if(heap.size() > size)
            heap.poll();
        return heap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
