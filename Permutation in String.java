class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length())
            return false;
        int [] s1Chars = new int [26];
        int [] s2Chars = new int [26];
        int left = 0;
        
        for(int i = 0; i < s1.length(); i++){
            s1Chars[s1.charAt(i) - 'a']++;
            s2Chars[s2.charAt(i) - 'a']++;
        }  
        for(int i = 0; i < s2.length() - s1.length(); i++){
            if(isSame(s1Chars, s2Chars))
                return true;
            s2Chars[s2.charAt(left++) - 'a']--;
            s2Chars[s2.charAt(i + s1.length()) - 'a']++;
        }
        return isSame(s1Chars, s2Chars);
    }
    public boolean isSame(int [] s1, int [] s2){
        for(int i = 0; i < 26; i++)
            if(s1[i] != s2[i])
                return false;
        return true;
    }
}
