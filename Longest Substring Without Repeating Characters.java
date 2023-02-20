class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0, left = 0, right = 0;
        Set<Character> seen = new HashSet<>();
        while(right < s.length()){
            while(seen.contains(s.charAt(right)))
                seen.remove(s.charAt(left++));
            seen.add(s.charAt(right));
            max = Math.max(max, right - left + 1);
            right++;
        }
        return max;
    }
}
//intiution
//use sliding window to keep track of the maximum window where there isnot a single repeating character
//window is valid if all the characters are non repeating
