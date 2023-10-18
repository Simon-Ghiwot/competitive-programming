// https://github.com/galencolin/cp-templates/blob/master/templates/trie.cpp
struct node {
	node* children[2];
	int cnt;
	node() {
		cnt = 0;
		children[0] = children[1] = nullptr;
	}
	node* next(int cur) {
		if (!children[cur]) children[cur] = new node;
		return children[cur];
	}
};
struct BIT_TRIE{
	node *root;
	BIT_TRIE(){
		root = new node();
	}
	void insert(int x) {
		node* traversor = root;
		for (int bit = 30; bit >= 0; bit--) {
			int v = !!(x & (1 << bit));
			traversor = traversor->next(v);
			traversor->cnt++;
		}
	}
	void remove(int x) {
		node* traversor = root;
		for (int bit = 30; bit >= 0; bit--) {
			int v = !!(x & (1 << bit));
			traversor = traversor->next(v);
			traversor->cnt--;
		}
	}
	int best(int x) { // best match
		node* traversor = root;
		int ans = 0;
		for(int bit = 30; bit >= 0; bit--){
			int v = (x & (1 << bit)) == 0;
			if (traversor->next(v)->cnt > 0) {
		     	traversor = traversor->next(v);
		     	if(v)	ans += (1 << bit);
		    } 
		    else {
			    traversor = traversor->next(!v);
			    if(!v)	ans += (1 << bit);
		    }
		}
		return ans;
	}
};
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        BIT_TRIE trie;
        int ans = 0;
        for(auto num : nums){
            trie.insert(num);
            int worst = trie.best(num);
            if((worst ^ num) > ans) ans = (worst ^ num);
        }
        return ans;
    }
};
