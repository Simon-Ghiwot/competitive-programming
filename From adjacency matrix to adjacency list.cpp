#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n;
	vector<vector<int>> edges(n);
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			int u;	cin >> u;
			if(u == 1)
				edges[i].push_back(j);
		}
	}
	for(int i = 0; i < n; i++){
		cout << (int) edges[i].size() << " ";
		for(auto to : edges[i]){
			cout << to + 1 << " ";
		}
		cout << ln;
	}
}

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
