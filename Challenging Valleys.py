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
	int valleys = 0;
	int i = 0;
	while(i < n){
		if(i == 0 || v[i] < v[i - 1]){
			while(i + 1 < n && v[i] == v[i + 1])
				i++;
			if(i + 1 >= n || v[i] < v[i + 1])
				valleys++;
		}
		i++;
	}
	cout << (valleys == 1 ? "YES" : "NO") << ln;
}	

int main(){
	int test = 1;
	cin >> test;
	while(test--){
		run_test_case();
	}
}
