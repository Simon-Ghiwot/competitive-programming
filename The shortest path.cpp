#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

const int nax = 50e4 + 400;

vector<int> edges[nax];

void run_test_case(){
	int a, b;
	cin >> n >> m >> a >> b;

	for(int i = 0; i < m; i++){
		int u, v;
		cin >> u >> v;
		edges[u].push_back(v);
		edges[v].push_back(u);
	}
	bool ok = false;
	vector<bool> visited(nax);
	vector<int> prev(nax);
	queue<int> que;
	visited[a] = true;
	que.push(a);
	while(!que.empty()){
		int size = (int) que.size();
		for(int i = 0; i < size; i++){
			int at = que.front(); que.pop();
			if(at == b){
				ok = true;
				break;
			}
			for(auto to : edges[at]){
				if(visited[to])	continue;
				visited[to] = true;
				que.push(to);
				prev[to] = at;
			}
		}
		if(ok)	break;
	}

	if(!ok){
		cout << -1 << ln;
		return;
	}
	vector<int> path;
	int at = b;
	path.push_back(at);
	while(at != a){
		at = prev[at];
		path.push_back(at);
	}
	reverse(path.begin(), path.end());
	cout << (int) path.size() - 1 << ln;
	for(int i = 0; i < (int) path.size(); i++)
		cout << path[i] << (i + 1 < (int) path.size() ? " " : "\n");
}	

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
