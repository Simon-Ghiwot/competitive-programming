class Solution {
    public List<Integer> partitionLabels(String s) {
        List<Integer> result = new ArrayList<>();
        int n = s.length(), i = 0;
        while (i < n){
            int last = s.lastIndexOf(s.charAt(i));
            for(int j = i; j < n && j < last; j++)
                last = Math.max(last, s.lastIndexOf(s.charAt(j)));
            
            result.add(last - i + 1);
            i = last + 1;
        }

        return result;
    }
}
