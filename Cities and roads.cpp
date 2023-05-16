#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n;
	int ans = 0;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			int u;	cin >> u;
			ans += u == 1;
		}
	}
	cout << ans / 2 << ln;
}

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
