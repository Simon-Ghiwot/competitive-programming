class MedianFinder {
    private PriorityQueue<Integer> maxHeap;
    private PriorityQueue<Integer> minHeap;
    public MedianFinder() {
        maxHeap = new PriorityQueue<>((a, b) -> b - a);//all element are less than the min heap element
        minHeap = new PriorityQueue<>();
    }
    private int getSize(){
        return maxHeap.size() + minHeap.size();
    }
    public void addNum(int num) {
        maxHeap.offer(num);
        minHeap.offer(maxHeap.poll());
        if(maxHeap.size() + 1 < minHeap.size())
            maxHeap.offer(minHeap.poll());
    }
    
    public double findMedian() {
        if(getSize() % 2 != 0)//if its odd then return the minimum from min heap
            return minHeap.peek();//because the largest elt in max heap is less than the smallest elt in min heap
        return (maxHeap.peek() + minHeap.peek()) / 2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
