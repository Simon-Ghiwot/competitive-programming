class Node{
public:
    int val;
    Node * children[26];
    Node(){
        val = 0;
        for(int i = 0; i < 26; i++) children[i] = nullptr;
    }
};
class MapSum {
public:
    Node * root;
    MapSum() {
        root = new Node();
    }
    
    void insert(string key, int val) {
        Node *traversor = root;
        for(char c : key){
            if(traversor->children[c - 'a'] == nullptr)
                traversor->children[c - 'a'] = new Node();
            traversor = traversor->children[c - 'a'];
        }
        traversor->val = val;
    }
    int dfs(Node * root){
        if(root == nullptr)
            return 0;
        int sum = root->val;
        for(int i = 0; i < 26; i++) if(root->children[i] != nullptr){
            sum += dfs(root->children[i]);
        }
        return sum;
    }
    int sum(string prefix) {
        Node *traversor = root;
        for(char c : prefix){
            if(traversor->children[c - 'a'] == nullptr) return 0;
            traversor = traversor->children[c - 'a'];
        }
        return dfs(traversor);
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
