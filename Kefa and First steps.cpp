#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n;
	vector<int> v(n);
	for(int i = 0; i < n; i++)	cin >> v[i];

	int result = 0, left = 0, right = 0;
	while(right < n){
		int current = v[right], left = right;
		while(right < n && current <= v[right]){
			current = v[right];
			right++;
		}
		result = max(result, right - left);
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
