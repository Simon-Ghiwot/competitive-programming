class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {

        Map<Integer, List<int []>> Nodes = new HashMap<>();
        for(int i = 0; i < times.length; i++){
            int src = times[i][0], dst = times[i][1], cost = times[i][2];
            if(!Nodes.containsKey(src - 1))
                Nodes.put(src - 1, new ArrayList<>());
            Nodes.get(src - 1).add(new int [] {dst - 1, cost});
        }
        
        int [] distance = dijkstra(Nodes, n, k);

        int result = Integer.MIN_VALUE;
        for(int i = 0; i < distance.length; i++){
            if(distance[i] == Integer.MAX_VALUE)
                return -1;    
            result = Math.max(distance[i], result);
        }
        return result;
    }
    private int [] dijkstra (Map<Integer, List<int []>> Nodes, int n, int k){
        PriorityQueue<int []> que = new PriorityQueue<>((a,b) -> a[1] - b[1]); 
        boolean [] visited = new boolean [n];
        int [] distance = new int[n];

        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[k - 1] = 0;
        que.offer(new int[] {k - 1, 0});
        while(!que.isEmpty()){
            int currentNode = que.peek()[0], currentCost = que.peek()[1];
            que.poll();
            if(visited[currentNode])    continue;
            visited[currentNode] = true;
            for(int [] newNode : Nodes.getOrDefault(currentNode, new ArrayList<>())){
                int dst = newNode[0], cost = newNode[1] + currentCost;
                if(!visited[dst] && cost < distance[dst]){
                    distance[dst] = cost;
                    que.offer(new int [] {dst, cost});
                }
            }

        }
        return distance;
    }
}
