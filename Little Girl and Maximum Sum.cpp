#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n >> q;
	vector<ll> v(n);
	vector<pair<int, int>> freq(n + 1), query;
	for(int i = 0; i < n; i++){
		cin >> v[i];
		freq[i].second = i;
	}	
	sort(v.begin(), v.end());
	reverse(v.begin(), v.end());
	for(int i = 0; i < q; i++){
		int s, e;
		cin >> s >> e;
		query.push_back({s, e});
		freq[s - 1].first++;
		freq[e].first--;
	}
	for(int i = 1; i < n + 1; i++)	freq[i].first += freq[i - 1].first;

	sort(freq.begin(), freq.end());
	reverse(freq.begin(), freq.end());

	vector<ll> pref(n + 1);

	for(int i = 0; i < n; i++)
		pref[freq[i].second + 1] = v[i];

	for(int i = 1; i < n + 1; i++)	pref[i] += pref[i - 1];

	ll ans = 0;
	for(int i = 0; i < q; i++){
		int s = query[i].first, e = query[i].second;

		ans += pref[e] - pref[s - 1];
	}

	cout << ans << ln;

}

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
