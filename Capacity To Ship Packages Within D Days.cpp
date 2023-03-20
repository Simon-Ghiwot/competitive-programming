// same problems as https://leetcode.com/problems/split-array-largest-sum/ already did that before
class Solution {
private:
    long long find_divison(vector<int> & v, long long mid){
        long long count = 1, sum = 0;
        for(int i = 0; i < v.size(); i++){
            if(sum + v[i] > mid){
                count++;
                sum = 0;
            }
            sum += v[i];
        }
        return count;
    }
public:
    int shipWithinDays(vector<int>& v, int k) {
        long long result = 1e18;
        long long left = *max_element(v.begin(), v.end()), right = 1e18;
    
        while(left <= right){
            long long mid = (left + right) / 2;
            int block = find_divison(v, mid);
    
            if(block > k)
                left = mid + 1;
            else{
                right = mid - 1;
                result = min(result, mid);
            }
        }
    
        return result;
    }
};
