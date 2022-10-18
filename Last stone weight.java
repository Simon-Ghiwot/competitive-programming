class Solution {
    public int lastStoneWeight(int[] stones) {
        if(stones == null || stones.length == 0)
            return 0;
        //use heap because we need to continually sort the element
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> b - a);
        for(int i = 0; i < stones.length; i++)
            heap.offer(stones[i]);
        while(heap.size() > 1){
            int y = heap.poll();
            int x = heap.poll();
            if(x != y)
                heap.offer(y - x);
        }
        return heap.size() == 0 ? 0 : heap.poll();
    }
}
