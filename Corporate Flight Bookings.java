class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] result = new int[n];
        for(int [] flight : bookings){
            result[flight[0] - 1] += flight[2];
            if(flight[1] < n)
                result[flight[1]] -= flight[2];
        }
        for(int i = 1; i < n; i++)
            result[i] += result[i - 1];
        return result;
    }
}
