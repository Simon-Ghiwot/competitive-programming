class Solution {
    public String removeKdigits(String num, int k) {
        //char[] chars = str.toCharArray();
        Stack<Character> stack = new Stack<>();

        for (char c : num.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.peek() > c) {
                stack.pop();
                k--;
            }
            if (!stack.isEmpty() || c != '0') 
                stack.push(c);
        }
        while (!stack.isEmpty() && k!= 0) {
            stack.pop();
            k--;
        }
        if (stack.isEmpty()) return "0";

        StringBuilder sb = new StringBuilder();
        //the iteration of ArrayDeque is from first to last.
        for (Character character : stack) {
            sb.append(character);
        }
        return sb.toString();
    }
}
