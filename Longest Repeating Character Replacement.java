class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0, right = 0, max = 0;
        int [] chars = new int [26];
        while(right < s.length()){
            chars[s.charAt(right) - 'A']++;
            while((right - left + 1) - maxCount(chars) > k)
                chars[s.charAt(left++) - 'A']--;
            max = Math.max(max, right - left + 1);
            right++;
        }
        return max;
    }
    private int maxCount(int [] chars){
        int max = chars[0];
        for(int i = 0; i < chars.length; i++)
            if(max < chars[i])
                max = chars[i];
        return max;
    }
}
