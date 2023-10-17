class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        map<string, int> store;
        for(string word : words)    store[word]++;
        int ans = 0;
        auto is_subsequence = [&](string cur){
            int cur_idx = 0;
            for(int i = 0; i < s.size() and cur_idx < cur.size(); i++){
                if(s[i] == cur[cur_idx])    cur_idx++;
            }
            return cur_idx == cur.size();
        };
        for(auto [word, freq] : store){
            ans += is_subsequence(word) * freq;
        }
        return ans;
    }
};
