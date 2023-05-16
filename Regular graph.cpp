#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n >> m;
	vector<int> degree(n);
	for(int i = 0; i < m; i++){
		int u, v;
		cin >> u >> v, u--, v--;
		degree[u]++;
		degree[v]++;
	}
	sort(degree.begin(), degree.end());
	if(degree[0] == degree.back())
		cout << "YES" << ln;
	else
		cout << "NO" << ln;
}

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
