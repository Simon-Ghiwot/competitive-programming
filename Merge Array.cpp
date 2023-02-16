/* stuff you should look for
 * int overflow, array bounds
 * special cases (n=1?)
 * do smth instead of nothing and stay organized
 * WRITE STUFF DOWN
 * DON'T GET STUCK ON ONE APPROACH
 */
#include<bits/stdc++.h>

using namespace std;

constexpr char ln = '\n';
constexpr int mod = 1e9 + 7;
constexpr long long MxN = 1e18;
constexpr int INF = 1e8;

int n, m, k;
string s, t;

void run_test_case(){
	cin >> n >> m;
	vector<long long> a(n), b(m);
	for(k = 0; k < n; k++)
		cin >> a[k];
	for(k = 0; k < m; k++)
		cin >> b[k];

	int i = 0, j = 0;
	vector<long long> v;
	while(i < n && j < m)
		if(a[i] < b[j])
			v.push_back(a[i++]);
		else
			v.push_back(b[j++]);

	while(i < n)
		v.push_back(a[i++]);
	while(j < m)
		v.push_back(b[j++]);
	for(k = 0; k < v.size(); k++)
		cout << v[k] << (k + 1 == n + m ? "" : " ");
}	
int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}
}
