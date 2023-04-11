#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
ll n, m, k, q;
string s, t;

int backtrack(int val){
	if(val > m){
		return -1;
	}
	if(val == m)
		return 0;

	ll by_two = backtrack(val * 2);
	ll by_three = backtrack(val * 3);

	if(by_three == -1 && by_two == -1)
		return -1;
	else if(by_three == -1)
		return by_two + 1;
	else if(by_two == -1)
		return by_three + 1;
	return min(by_three, by_two) + 1;
}

void run_test_case(){
	cin >> n >> m;
	ll result = backtrack(n);
	cout << result << ln;
}

int main(){

	int test = 1;
	// cin >> test;

	while(test--){
		run_test_case();
	}	
}
