class MinStack {
    private Stack<Integer> elements;
    private Stack<Integer> min;
    public MinStack() {
        min = new Stack<>();
        elements = new Stack<>();
    }
    
    public void push(int val) {
        if(elements.isEmpty())
            min.push(val);
        else{
            int currentMin = min.peek();
            if(currentMin > val)
                currentMin = val;
            min.push(currentMin);
        }
        elements.push(val); 
    }
    
    public void pop() {
        elements.pop();
        min.pop();
    }
    
    public int top() {
        return elements.peek();
    }
    
    public int getMin() {
        return min.peek();
    }
}
