class Solution {
    public int fib(int n) {
        if(n <= 0)
            return 0;
        if(n <= 2)
            return 1;
        int [] result = new int [n + 1];
        result[1] = result[2] = 1;
        for(int i = 3; i < result.length; i++){
            result[i] = result[i - 1] + result[i - 2];
        }
        return result[n];
    }
}
