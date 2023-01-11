class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> anagram = new HashMap<>();
        
        for(String current : strs){
            char [] curr = current.toCharArray();
            Arrays.sort(curr);
            String strCurr = new String(curr);
            if(!anagram.containsKey(strCurr))
                anagram.put(strCurr, new ArrayList<>());
            anagram.get(strCurr).add(current);
        }
        result.addAll(anagram.values());
        return result;
    }
}
