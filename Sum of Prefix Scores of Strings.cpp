// same problem as https://leetcode.com/problems/map-sum-pairs/description/
class Node{
public:
    int cnt;
    Node * children[26];
    Node(){
        cnt = 0;
        for(int i = 0; i < 26; i++) children[i] = nullptr;
    }
};
class Solution {
public:
    void insert(string word, Node * root) {
        Node *traversor = root;
        for(char c : word){
            if(traversor->children[c - 'a'] == nullptr)
                traversor->children[c - 'a'] = new Node();
            traversor = traversor->children[c - 'a'];
            traversor->cnt++;
        }
    }
    vector<int> sumPrefixScores(vector<string>& words) {
        Node * root = new Node();
        vector<int> ans(words.size());
        
        auto calc = [&](string & word){
            Node * traversor = root;
            int res = 0;
            for(auto c : word){
                traversor = traversor->children[c - 'a'];
                res += traversor->cnt;
            }  
            return res;
        };
        for(auto word : words) insert(word, root);
        for(int i = 0; i < words.size(); i++){
            string word = words[i];
            ans[i] = calc(word);
        }

        return ans; 
    }
};
