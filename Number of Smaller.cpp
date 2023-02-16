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

	vector<long long> v;
	int j = 0, prev = 0;
	for(int i = 0; i < m; i++){
		int count = 0;
		for(; j < n; j++){
			if(a[j] >= b[i])
				break;
			count++;
		}
		prev += count;
		v.push_back(prev);
	}
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
