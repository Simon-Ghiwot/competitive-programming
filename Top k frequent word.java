class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        List<String> result = new ArrayList<>();

        Map<String, Integer> map = new HashMap<>();
        for(int i = 0; i < words.length; i++)
            map.put(words[i], map.getOrDefault(words[i], 0) + 1);

        PriorityQueue<String> [] heap = new PriorityQueue[words.length + 1];

        for(String current : map.keySet()){
            int index = map.get(current);
            if(heap[index] == null)
                heap[index] = new PriorityQueue<>();
            heap[index].offer(current);
        }
        for(int i = words.length; i >= 0 && result.size() != k; i--){
            if(heap[i] == null) continue;
            while(heap[i].size() != 0 && result.size() != k)
                result.add(heap[i].poll());
        }
        return result;
    }
}
