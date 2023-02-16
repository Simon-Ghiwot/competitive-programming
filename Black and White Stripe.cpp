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
	cin >> n >> k;
	cin >> s;

	int left = 0, white = 0;
	for(int i = 0; i < k; i++)
		if(s[i] == 'W')
			white++;
	int result = white;
	for(int i = k; i < n; i++){
		if(s[left] == 'W')
			white--;

		if(s[i] == 'W')
			white++;

		left++;
		result = min(result, white);
	}
	cout << result << ln;	
}	
int main(){
	int test = 1;
	cin >> test;
	while(test--){
		run_test_case();
	}
}
