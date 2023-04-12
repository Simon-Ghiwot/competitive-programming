// similar to https://cses.fi/problemset/task/1662 reason for the code being cpp
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        map<int, int> past_mod;
        past_mod[0]++;
        int running_sum = 0, result = 0;
        for(int i = 0; i < nums.size(); i++){
            running_sum += nums[i] % k;
            running_sum = (running_sum + k) % k;
            result += past_mod[running_sum];
            past_mod[running_sum]++;
        }
        return result;
    }
};
