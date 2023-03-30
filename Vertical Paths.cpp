#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;
int root;

void dfs(int at, int parent, vector<vector<int>> & result, vector<int> & cur, vector<vector<int>> & edges){
	bool went = false;
	for(auto to : edges[at]){
		if(to == parent)	continue;
			
		if(!went){
			cur.push_back(to + 1);
			dfs(to, at, result, cur, edges);
			went = 1 ^ went;
		}
		else{
			vector<int> new_cur = { to + 1 };
			dfs(to, at, result, new_cur, edges);
		}
	}
	if(edges[at].size() == 1 && at != root){
		result.push_back(cur);
	}
}

void run_test_case(){
	cin >> n;
	vector<vector<int>> edges(n);
	vector<vector<int>> result;

	for(int v = 0; v < n; v++){
		int u;
		cin >> u, u--;
		if(v != u){
			edges[v].push_back(u);
			edges[u].push_back(v);
		}
		else	
			root = v;
	}
	vector<int> cur = { root + 1 };
	dfs(root, -1, result, cur, edges);

	if(n == 1){
		cout << 1 << ln << 1 << ln << 1 << ln;
		return;
	}
	cout << result.size() << ln;
	for(int i = 0; i < result.size(); i++){
		cout << result[i].size() << ln;
		for(int j = 0; j < result[i].size(); j++)
			cout << result[i][j] << (j + 1 < result[i].size() ? " " : "\n");
	}
}

int main(){
	int test = 1;
	cin >> test;
	while(test--){
		run_test_case();
	}	
}
