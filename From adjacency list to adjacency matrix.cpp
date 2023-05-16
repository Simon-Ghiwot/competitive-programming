#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

int v[101][101];

void run_test_case(){
	cin >> n;
	for(int i = 0; i < n; i++){
		int x;	cin >> x;
		for(int j = 0; j < x; j++){
			int u;	cin >> u, u--;
			v[i][u] = 1;
		}
	}
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			cout << v[i][j] << (j + 1 < n ? " " : "\n");
}

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
