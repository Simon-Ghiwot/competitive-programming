class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        for(Character c : s.toCharArray()){
            if(c != ']')
                stack.push(c);
            else{
                StringBuilder current = new StringBuilder();
                while(!stack.isEmpty() && stack.peek() != '[')
                    current.append(stack.pop());
                stack.pop();
                current.reverse();
                StringBuilder repeat = new StringBuilder();
                while(!stack.isEmpty() && Character.isDigit(stack.peek()))
                    repeat.append(stack.pop());
                int time = Integer.parseInt(new String(repeat.reverse()));
                for(int i = 0; i < time; i++)
                    for(Character l : current.toString().toCharArray())
                        stack.push(l);
            }
        }
        StringBuilder result = new StringBuilder();
        while(!stack.isEmpty())
            result.append(stack.pop());
        return new String(result.reverse());
    }
}
