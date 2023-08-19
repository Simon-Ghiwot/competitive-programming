class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums, int x) {
        if(x == 0)
            return 0;
        vector<int> check;
        multiset<int> store;
        for(int i = nums.size() - 1 - x; i >= 0; i--)   store.insert(nums[i]);
        for(int i = nums.size() - 1; i > nums.size() - 1 - x; i--)  check.push_back(nums[i]);
        
        long long ans = 1e18, idx = 0, window = nums.size() - 1 - x;

        while(!store.empty()){
            auto it = store.lower_bound(check[idx]);

            long long left = it == store.end() ? 1e18 : *it;
            long long right = it != store.begin() ? *prev(it) : 1e18;
            
            ans = min({ans, abs(check[idx] - right), abs(check[idx] - left)});
            it = store.find(nums[window]);
            store.erase(it);
            check.push_back(nums[window--]);
            idx++;
        }
        return ans;
    }
};
