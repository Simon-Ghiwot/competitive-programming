#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

const int nax = 2e5 + 200;

void run_test_case(){
	cin >> n >> k >> q;
	vector<int> v(nax), pref(nax);
	for(int i = 0; i < n; i++){
		int s, e;
		cin >> s >> e;
		v[s]++;
		v[e + 1]--;
	}
	for(int i = 1; i < nax; i++) v[i] += v[i - 1];

	for(int i = 0; i < nax; i++)	pref[i] = v[i] >= k;
	for(int i = 1; i < nax; i++)	pref[i] += pref[i - 1];

	for(int i = 0; i < q; i++){
		int s, e;
		cin >> s >> e;
		cout << pref[e] - pref[s - 1] << ln;
	}
}

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
