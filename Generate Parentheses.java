class Solution {
    private List<String> result;
    public List<String> generateParenthesis(int n) {
        result = new ArrayList<>();
        backtrack(0, 0, n, "");
        return result;
    }
    private void backtrack(int open, int close, int size, String current){
        if(close == open && open == size){
            result.add(current);
            return;
        }
        if(open < size)
            backtrack(open + 1, close, size, current + "(");
        if(close < open)
            backtrack(open, close + 1, size, current + ")");
    }
}
