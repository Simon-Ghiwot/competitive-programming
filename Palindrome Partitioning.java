class Solution {
    private List<List<String>> result;
    public List<List<String>> partition(String s) {
        result = new ArrayList<>();
        backtracking(0, new ArrayList<>(), s);
        return result;
    }
    private void backtracking(int start, List<String> current, String s){
        if(start >= s.length())
            result.add(new ArrayList<>(current));
        for(int i = start; i < s.length(); i++){
            if(!isPalindrome(s, start, i))  continue;//check if the partition is a palidrome/is valid partitioning
            current.add(s.substring(start, i + 1));
            backtracking(i + 1, current, s);
            current.remove(current.size() - 1);
        }
    }
    boolean isPalindrome(String s, int low, int high) {
        while (low < high) 
            if (s.charAt(low++) != s.charAt(high--)) return false;
        return true;
    }
}
