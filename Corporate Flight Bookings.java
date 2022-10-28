class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int [] result = new int [n];
        
        for(int i = 0; i < bookings.length; i++){
            for(int j = bookings[i][0]; j <= bookings[i][1]; j++){
                result[j - 1] += bookings[i][2]; 
            }
        }
        return result;
    }
}
