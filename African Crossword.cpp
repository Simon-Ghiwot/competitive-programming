#include<bits/stdc++.h>

using namespace std;

constexpr char ln = '\n';
constexpr int mod = 1e9 + 7;
constexpr long long MxN = 1e18;

int n, m, k;
string s, t;

void run_test_case(){
	cin >> n >> m;
	vector<string> v(n);
	for(int i = 0; i < n; i++)
		cin >> v[i];
	vector<vector<bool>> correct(n, vector<bool>(m, true));

	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			bool ok = true;
			for(int k = 0; k < m; k++){
				if(k == j)	continue;
				if(v[i][j] == v[i][k]){
					correct[i][k] = false;
					ok = false;
				}
			}
			for(int k = 0; k < n; k++){
				if(k == i)	continue;
				if(v[k][j] == v[i][j]){
					ok = false;
					correct[k][j] = false;
				}
			}
			correct[i][j] = ok;
		}
	}
	string result = "";
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if(correct[i][j])
				result += v[i][j];
	cout << result;
}	

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}
}
