#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;


void run_test_case(){
	ll n, m;
	cin >> n >> m;

	ll left = 0, right = min(n, m);
	while(left <= right){
		ll mid = (left + right) / 2;
		if(mid * 4 <= n + m)
			left = mid + 1;
		else
			right = mid - 1;
	}
	cout << right << ln;
}

int main(){
	int test = 1;
	cin >> test;
	while(test--){
		run_test_case();
	}
}
