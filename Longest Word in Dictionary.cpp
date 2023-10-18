class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        string ans = "";
        set<string> store = { "" };
        for(auto word : words){
            string sub = word.substr(0, word.size() - 1);
            if(store.find(sub) != store.end()){
                store.insert(word);
                if(word.size() > ans.size()) ans = word;
            }
        }
        return ans;
    }
};
