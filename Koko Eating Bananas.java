class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int right = piles[0], left = 1;
        for(int i = 0; i < piles.length; i++)
            if(right < piles[i])
                right = piles[i];
        
        while(left <= right){
            int mid = (left + right)/2, hourSpent = 0;
            for(int i = 0; i < piles.length; i++)
                hourSpent += Math.ceil((double) piles[i]/mid);
            if(hourSpent <= h)
                right = mid - 1;
            else
                left = mid + 1; 
        }
        return  left;
    }
}
