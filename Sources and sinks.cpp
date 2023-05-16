#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n;
	vector<int> out(n), in(n);
	int sink = 0, source = 0;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			int u;	cin >> u;
			if(u == 1){
				in[j]++;
				out[i]++;
			}
		}
	}
	for(int i = 0; i < n; i++){
		if(in[i] == 0)
			source++;
		if(out[i] == 0)
			sink++;
	}
	cout << source << " ";
	for(int i = 0; i < n; i++)	if(in[i] == 0){
		cout << i + 1 << " ";
	}
	cout << ln << sink << " ";
	for(int i = 0; i < n; i++)	if(out[i] == 0){
		cout << i + 1 << " ";
	}
	cout << ln;
}

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
