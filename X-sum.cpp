#include<bits/stdc++.h>

using namespace std;

constexpr char ln = '\n';
constexpr int mod = 1e9 + 7;
constexpr long long MxN = 1e18;

int n, m;

int find_sum(vector<vector<int>> & board, int i, int j){
	int sum = board[i][j];

	int directions [4][2] = {{-1, -1}, {1, 1}, {-1, 1}, {1, -1}};

	for(auto dir : directions){
		int row = i + dir[0], col = j + dir[1];
		while (row >= 0 && col >= 0 && row < n && col < m){
			sum += board[row][col];
			row += dir[0];
			col += dir[1];
		}
	}
	return sum;
}

void run_test_case(){

    cin >> n >> m;

    vector<vector<int>> board(n, vector<int>(m));

    for(int i = 0; i < n; i++)
    	for(int j = 0; j < m; j++)
    		cin >> board[i][j];

    int result = 0;
    
    for(int i = 0; i < n; i++)
    	for(int j = 0; j < m; j++)
    		result = max(result, find_sum(board, i, j));
    	
    cout << result << ln;
}	

int main(){
	int test = 1;
	cin >> test;
	while(test--){
		run_test_case();
	}
}
