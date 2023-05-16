eolymp
ProblemsQueueCompetitionsRankingGroupsArticlesFund

Solutions
#13754531
Results
Source code

Problem
Operations on graph
Submitted
9 seconds ago
Programming Language
C++ 17 (gnu 10.2)
Author
simon_ghiwot
100%C
211 ms
4.92 MiB
Your submission was graded C, which means it passed all tests and used LESS resources than 50% of the submissions on the website.
Test #	Status	Score	Duration	CPU	Memory

Test suite #1
Accepted	100 / 100	211 ms	211 ms	5,036 KiB

Test #1
Accepted	12 / 12	1 ms	1 ms	584 KiB

Test #2
Accepted	12 / 12	1 ms	1 ms	580 KiB

Test #3
Accepted	12 / 12	2 ms	2 ms	628 KiB

Test #4
Accepted	12 / 12	211 ms	211 ms	5,036 KiB

Test #5
Accepted	13 / 13	33 ms	33 ms	1,484 KiB

Test #6
Accepted	13 / 13	10 ms	9 ms	732 KiB

Test #7
Accepted	13 / 13	96 ms	96 ms	3,236 KiB

Test #8
Accepted	13 / 13	92 ms	92 ms	4,400 KiB
100 / 100	211 ms	211 ms	5,036 KiB
Source code content_copy
#include<bits/stdc++.h>
 
#define ll long long
 
using namespace std;
 
const char ln = '\n';
 
int n, m, k, q;
string s, t;

void run_test_case(){
	cin >> n >> k;
	vector<vector<int>> edges(n + 1);
	for(int i = 0; i < k; i++){
		int type;	cin >> type;
		if(type == 2){
			int u;	 cin >> u;
			for(auto to : edges[u]){
				cout << to << " ";
			}
			if((int) edges[u].size())
				cout << ln;
		}
		else{
			int u, v;
			cin >> u >> v;
			edges[u].push_back(v);
			edges[v].push_back(u);
		}
	}
}

int main(){
	int test = 1;
	// cin >> test;
	while(test--){
		run_test_case();
	}	
}
© Eolymp 2023
NewsFeedbackHelpAboutPrivacy NoticeTerms of UseFundBlog
Language: English
