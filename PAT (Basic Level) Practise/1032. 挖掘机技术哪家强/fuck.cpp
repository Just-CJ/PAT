#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

bool mycmp(pair<int, int> p1, pair<int, int> p2){
	return p1.second < p2.second;
}

int main(){
	int num;
	scanf("%d", &num);
	map<int, int> scoreboard;
	for (int i = 0; i < num; i++){
		int id, score;
		scanf("%d%d", &id, &score);
		if (scoreboard.find(id) != scoreboard.end()){
			scoreboard[id] += score;
		}
		else{
			scoreboard[id] = score;
		}
	}

	map<int, int>::iterator it;
	it = max_element(scoreboard.begin(), scoreboard.end(), mycmp);
	printf("%d %d", (*it).first, (*it).second);
	return 0;
}