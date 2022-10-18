class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if(p.length() > s.length())
            return result;
        int [] first = new int [26];
        int [] second = new int [26];
        
        for(int i = 0; i < p.length(); i++){
            first[p.charAt(i) - 'a']++;
            second[s.charAt(i) - 'a']++;
        }
        for(int i = 0; i < s.length() - p.length(); i++){
            if(isSame(first, second))
                result.add(i);
            second[s.charAt(i) - 'a']--;
            second[s.charAt(i + p.length()) - 'a']++;
        }
        if(isSame(first, second))
            result.add(s.length() - p.length());
        
        return result;
    }
    private boolean isSame(int [] first, int [] second){
        for(int i = 0; i < 26; i++)
            if(first[i] != second[i])
                return false;
        return true;
    }
}
