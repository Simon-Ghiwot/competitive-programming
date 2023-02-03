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
long long count(vector<long long> & v, int mid){
	long long counter = 0;
	for(auto val : v){
		if(val <= mid)
			counter++;
	}
	return counter;
}
 
void run_test_case(){
	cin >> n >> k;
	vector<long long> v(n);
	for(int i = 0; i < n; i++)
		cin >> v[i];
	sort(v.begin(), v.end());
 
	long long left = 1, right = v[n - 1];
	long long result = -1;
	while(left <= right){
		long long mid = (right + left) / 2;
		// cout << mid << " :: mid " << ln;
		long long how_many = count(v, mid);
		// cout << how_many << " :: how_many " << ln;
		if(how_many > k)
			right = mid - 1;
		else if(how_many < k)
			left = mid + 1;
		else{
			result = mid;
			break;
		}
	}
 
 
	cout << result << ln;
}	
int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}
}
