class Node{
public:
    bool isWord;
    Node *children[26];
    Node(){
        isWord = false;
        for(int i = 0; i < 26; i++) children[i] = nullptr;
    }
};
class WordDictionary {
public:
    Node *root;
    WordDictionary() {
        root = new Node();
    }
    
    void addWord(string word) {
        Node *traversor = root;
        for(char c : word){
            if(traversor->children[c - 'a'] == nullptr)
                traversor->children[c - 'a'] = new Node();
            traversor = traversor->children[c - 'a'];
        }
        traversor->isWord = true;
    }
    bool backtrack(string word, int idx, Node * root){
        if(idx == word.size()) return root->isWord;

        if(word[idx] == '.'){
            bool is_possible = false;
            for(int i = 0; i < 26; i++) if(root->children[i] != nullptr){
                if(backtrack(word, idx + 1, root->children[i])) return true;
            }
            return false;
        }
        else if(root->children[word[idx] - 'a'] == nullptr)  return false;

        return backtrack(word, idx + 1, root->children[word[idx] - 'a']);
    }
    bool search(string word) {
        return backtrack(word, 0, root);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
