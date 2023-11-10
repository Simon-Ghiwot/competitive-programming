#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n >> m;
	vector<set<int>> rail(n), road(n);
	for(int i = 0; i < m; i++){
		int u, v;
		cin >> u >> v, u--, v--;
		rail[u].insert(v);
		rail[v].insert(u);
	}
	for(int i = 0; i < n; i++){
		for(int j = i + 1; j < n; j++){
			if(rail[i].find(j) == rail[i].end()){
				road[i].insert(j);
				road[j].insert(i);
			}
		}
	}
	vector<int> vis_rail(n, -1), vis_road(n, -1);
	queue<int> que, road_que;
	que.push(0);
	vis_rail[0] = 0;
	int time = 0, found = 0;
	while(!que.empty()){
		int size = que.size();
		for(int i = 0; i < size; i++){
			int at = que.front(); que.pop();
			if(at == n - 1){
				time = vis_rail[at];
				found = 1;
				break;
			}
			for(auto & to : rail[at]){
				if(vis_rail[to] == -1){
					vis_rail[to] = vis_rail[at] + 1;
					que.push(to);
				}
			}
		}
		if(found == 1)	break;
	}
	road_que.push(0);
	vis_road[0] = 0;
	int time_2 = -1;
	found = 0;
	while(!road_que.empty()){
		int size = road_que.size();
		for(int i = 0; i < size; i++){
			int at = road_que.front(); road_que.pop();
			if(at == n - 1){
				time_2 = vis_road[at];
				found = 1;
				break;
			}
			if(vis_road[at] == vis_rail[at] and at != 0)	continue;
			for(auto & to : road[at]){
				if(vis_road[to] == -1){
					vis_road[to] = vis_road[at] + 1;
					road_que.push(to);
				}
			}
		}
		if(found == 1)	break;
	}
	time = max(time, time_2);
	if(vis_rail[n - 1] == -1 or vis_road[n - 1] == -1)
		cout << -1 << ln;
	else
		cout << time << ln;
}	
int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
