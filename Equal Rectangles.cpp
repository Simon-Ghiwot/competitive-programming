#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n;
	vector<ll> v(4 * n);
	for(int i = 0; i < 4 * n; i++)	cin >> v[i];

	sort(v.begin(), v.end());
	for(int i = 0; i < 4 * n; i += 2) if(v[i] != v[i + 1]){
		cout << "NO" << ln;
		return;
	}
	ll area = v[0] * v[4 * n - 1];
	int right = 4 * n - 1, left = 0;
	while(left < right){
		if(v[left] * v[right] != area){
			cout << "NO" << ln;
			return;
		}
		left += 2;
		right -= 2;
	}

	cout << "YES" << ln;
	return;
}

int main(){

	int test = 1;
	cin >> test;

	while(test--){
		run_test_case();
	}	
}
