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
	cin >> n;
	vector<long long> v(n);
	int even = 0, odd = 0;
	for(int i = 0; i < n; i++){
		cin >> v[i];
		if(v[i] % 2 == 0)
			even++;
		else
			odd++;
	}
	if(odd > 0 && even > 0)
		sort(v.begin(), v.end());

	for(int i = 0; i < n; i++)
		cout << v[i] << (i + 1 == n ? "\n" : " ");

}	
int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}
}
