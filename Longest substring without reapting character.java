class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0, left = 0, right = 0;
        Set<Character> seen = new HashSet<>();
        while(right < s.length()){
            while(seen.contains(s.charAt(right)))
                seen.remove(s.charAt(left++));
            seen.add(s.charAt(right++));
            max = Math.max(max, right - left);
        }
        return max;
    }
}
