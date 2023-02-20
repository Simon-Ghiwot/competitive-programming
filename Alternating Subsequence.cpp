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

int n, m, k;
string s, t;

void run_test_case(){
	cin >> n;
	vector<long long> v(n);
	for(int i = 0; i < n; i++)
		cin >> v[i];
	long long ans = 0;
	int i = 0;
	for(int i = 0; i < n; i++){
		long long cur_max = v[i];
		while(i + 1 < n && (v[i] < 0 && v[i + 1] < 0 || v[i] > 0 && v[i + 1] > 0)){
			cur_max = max(cur_max, v[i]);
			i++;
		}
		cur_max = max(cur_max, v[i]);
		ans += cur_max;
	}
	cout << ans << ln;
}	
int main(){
	int test = 1;
	cin >> test;
	while(test--){
		run_test_case();
	}
}
