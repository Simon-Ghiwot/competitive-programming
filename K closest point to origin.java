class Solution {
    public int[][] kClosest(int[][] points, int k) {
        List<int []> result = new ArrayList<>();
        PriorityQueue<int []> heap = new PriorityQueue<>//declaring a min heap
        ((a, b) ->  Integer.compare(
                    (a[0] * a[0] + a[1] * a[1]),
                    (b[0] * b[0] + b[1] * b[1])
                )
        );
        
        for(int i = 0; i < points.length; i++)
            heap.offer(points[i]);
        for(int i = 0; i < k; i++)
            result.add(heap.poll());
        return result.toArray(new int[result.size()][2]);
    }
}
