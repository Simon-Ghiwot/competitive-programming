#include<bits/stdc++.h>

using namespace std;

constexpr char ln = '\n';
constexpr int mod = 1e9 + 7;
constexpr long long MxN = 1e18;

int n, m, k;
string s, t;

void run_test_case(){
	long long d;
	cin >> n >> d;
	vector<long long> v(n);
	for(int i = 0; i < n; i++)
		cin >> v[i];

	sort(v.begin(), v.end());
	int right = n - 1, left = 0;
	int result = 0;

	while(left <= right){
		if(left == right){
			if(v[right] > d)
				result++;
		}
		else if(v[right] > d)
			result++;		
		else{
			int count = 1;
			while(left < right && count * v[right] <= d){
				left++;
				// cout << "left " << left << ln;
				count++;
			}
			// cout << count   <<ln;
			if(count * v[right] > d)
				result++;
		}
		right--;
	}
	cout << result;
}	

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}
}
