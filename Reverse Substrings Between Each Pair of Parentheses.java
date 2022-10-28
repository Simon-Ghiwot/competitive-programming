class Solution {
    public String reverseParentheses(String s) {
        Stack<Character> stack = new Stack<>();
        Queue<Character> que = new LinkedList<>();
         for(int i = 0; i < s.length(); i++){
             if(s.charAt(i) == ')'){
                 while(!stack.isEmpty() && stack.peek() != '(')
                    que.offer(stack.pop());
                if(!stack.isEmpty())
                    stack.pop();
                while(!que.isEmpty())
                    stack.push(que.poll());
             }
             else
                stack.push(s.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty())
            sb = sb.append(stack.pop());
        return new String(sb.reverse());
    }
}
