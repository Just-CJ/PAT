#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <map>
#include <algorithm>
using namespace std;




bool mycmp(const pair<char, int> &p1, const pair<char, int> &p2){
	if (p1.second < p2.second)
		return true;
	else if (p1.second == p2.second)
		return p1.first > p2.first;
	else
		return false;
}

int main()
{
	int num;
	scanf("%d", &num);
	int win = 0, draw = 0, lose = 0;
	map<char, int> dict_A, dict_B;
	dict_A.insert(make_pair('B', 0));
	dict_A.insert(make_pair('C', 0));
	dict_A.insert(make_pair('J', 0));
	dict_B.insert(make_pair('B', 0));
	dict_B.insert(make_pair('C', 0));
	dict_B.insert(make_pair('J', 0));
	for (int i = 0; i < num; i++){
		char A, B;
		A = getchar();
		while (A == ' ' || A == '\n')
			A = getchar();
		B = getchar();
		while (B == ' ' || B == '\n')
			B = getchar();
		if (A == B){
			draw++;
		}
		else if ((A == 'C' && B == 'J') || (A == 'J' && B == 'B') || (A == 'B' && B == 'C')){
			win++;
			dict_A[A]++;
		}
		else{
			lose++;
			dict_B[B]++;
		}

	}
	printf("%d %d %d\n", win, draw, lose);
	printf("%d %d %d\n", lose, draw, win);
	map<char, int>::iterator it;
	it = max_element(dict_A.begin(), dict_A.end(), mycmp);
	printf("%c ", (*it).first);
	it = max_element(dict_B.begin(), dict_B.end(), mycmp);
	printf("%c", (*it).first);
	

	return 0;
}