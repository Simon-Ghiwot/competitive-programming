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

	int count_two = 0;
	for(int i = 0; i < n; i++){
		while(v[i] % 2 == 0){
			count_two++;
			v[i] /= 2;
		}
	}
	if(count_two >= n){
		cout << 0 << ln;
		return;
	}
	vector<int> indexs;
	for(int i = 2; i <= n; i += 2){
		int count_index = 0, idx = i;
		while(idx % 2 == 0){
			count_index++;
			idx /= 2;
		}
		indexs.push_back(count_index);
	}
	sort(indexs.begin(), indexs.end());
	reverse(indexs.begin(), indexs.end());
	for(int i = 0; i < (int) indexs.size(); i++){
		count_two += indexs[i];
		if(count_two >= n){
			cout << i + 1 << ln;
			return;
		}
	}
	cout << -1 << ln;
}

int main(){
	int test = 1;
	cin >> test;
	while(test--){
		run_test_case();
	}	
}
