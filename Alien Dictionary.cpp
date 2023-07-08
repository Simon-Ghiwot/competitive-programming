class Solution{
    public:
    string findOrder(string v[], int n, int K) {
        vector<vector<int>> edges(26);
    	vector<int> indegree(26);
    	for(int i = 0; i < n - 1; i++){
    		bool found = false;
    		for(int j = 0; j < min(v[i + 1].length(), v[i].length()); j++){
    			if(v[i][j] != v[i + 1][j]){
    				edges[v[i][j] - 'a'].push_back(v[i + 1][j] - 'a');
    				indegree[v[i + 1][j] - 'a']++;
    				found = true;
    				break;
    			}
    		}
    		if(!found and v[i].length() > v[i + 1].length())    return "";
    	}
    	queue<int> que;
    	vector<int> ans;
    	for(int i = 0; i < 26; i++){
    		if(indegree[i] == 0)
    			que.push(i);
    	}
     
    	while(!que.empty()){
    		int at = que.front(); que.pop();
    		ans.push_back(at);
    		for(auto to : edges[at]){
    			indegree[to]--;
    			if(indegree[to] == 0)
    				que.push(to);
    		}
    	}
    	if(ans.size() != 26)    return "";
    	string res = string(26, '?');
    	for(int i = 0; i < 26; i++)
		    res[i] = (char) (ans[i] + 'a');
		   return res;
		    
    	
    }
};
