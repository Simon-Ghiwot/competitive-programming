class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        //solved using monothonic decreasing stack;
        int [] result = new int [temperatures.length];//default value is 0
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < temperatures.length; i++){
            while(!stack.isEmpty() && temperatures[stack.peek()] < temperatures [i]){
                int index = stack.pop();
                result[index] = i - index;//calculating the distance
            }
            stack.push(i);
        }
        return result;
    }
}
