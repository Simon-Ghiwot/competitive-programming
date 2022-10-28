class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> b - a);
        for(int i = matrix.length - 1; i >= 0; i--)
            for(int j = matrix.length - 1; j >= 0; j--){
                heap.offer(matrix[i][j]);
                if(heap.size() > k)
                    heap.poll();
            }
        return heap.poll();
    }
}
