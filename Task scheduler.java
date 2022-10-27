class Solution {
    public int leastInterval(char[] tasks, int n) {
        if(n == 0)
            return tasks.length;
            
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < tasks.length; i++)
            map.put(tasks[i], map.getOrDefault(tasks[i], 0) + 1);

        PriorityQueue<Pair<Character, Integer>> task = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        Queue<Pair<Character, Integer>> que = new LinkedList<>();
        Queue<Integer> waitingQue = new LinkedList<>();

        for(Character c : map.keySet())
            task.offer(new Pair<>(c, map.get(c)));

        int interval = 0;
        while(!que.isEmpty() || !task.isEmpty()){
            if(!que.isEmpty() && interval - waitingQue.peek() == n + 1){
                task.offer(que.remove());
                waitingQue.remove();
            }
            if(!task.isEmpty()){
                Pair<Character, Integer> pair = task.poll();
                int value = pair.getValue() - 1;
                Pair<Character, Integer> newPair = new Pair<>(pair.getKey(), value);
                if(newPair.getValue() != 0){
                    que.add(newPair);
                    waitingQue.add(interval);
                }
            }
            interval++;
        }
        
        return interval;
    }
}

