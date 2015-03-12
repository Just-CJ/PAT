#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

class model{
public:
	int id;
	int score1;
	int score2;
	model(){
		model(0, 0, 0);
	}
	model(int id, int score1, int score2){
		this->id = id;
		this->score1 = score1;
		this->score2 = score2;
	}


};


bool mycmp(const model &m1, const model &m2){
	if ((m1.score1 + m1.score2)>(m2.score1 + m2.score2))
		return true;
	else if ((m1.score1 + m1.score2) == (m2.score1 + m2.score2)){
		if (m1.score1 > m2.score1)
			return true;
		else if (m1.score1 == m2.score1)
			return m1.id < m2.id;
	}

	return false;
}
/*
int mycmp(const void *m11, const void *m22 ){
	model *m1 = (model*)m11;
	model *m2 = (model*)m22;
	if ((m1->score1 + m1->score2)>(m2->score1 + m2->score2))
		return -1;
	else if ((m1->score1 + m1->score2) == (m2->score1 + m2->score2)){
		if (m1->score1 > m2->score1)
			return -1;
		else if (m1->score1 == m2->score1)
			return m1->id - m2->id;
	}

	return 1;
}*/

int main()
{
	int num, low, high;
	cin>>num>>low>>high;

	vector<model> A, B, C, D;
	//model A[100000], B[100000], C[100000], D[100000];
	//int A_num = 0, B_num = 0, C_num = 0, D_num = 0;

	for (int i = 0; i < num; i++){
		int id, score1, score2;
		cin >> id >> score1 >> score2;
		if (score1 >= low && score2 >= low){
			if (score1 >= high && score2 >= high){
				model tmp(id, score1, score2);
				//A[A_num] = tmp;
				//A_num++;
				A.push_back(tmp);
			}
			else if (score1 >= high){
				model tmp(id, score1, score2);
				//B[B_num] = tmp;
				//B_num++;
				B.push_back(tmp);
			}
			else if (score1 >= score2){
				model tmp(id, score1, score2);
				//C[C_num] = tmp;
				//C_num++;
				C.push_back(tmp);
			}
			else{
				model tmp(id, score1, score2);
				//D[D_num] = tmp;
				//D_num++;
				D.push_back(tmp);
			}
		}
	}

	//qsort(A, A_num, sizeof(model), mycmp);
	//qsort(B, B_num, sizeof(model), mycmp);
	//qsort(C, C_num, sizeof(model), mycmp);
	//qsort(D, D_num, sizeof(model), mycmp);
	sort(A.begin(), A.end(), mycmp);
	sort(B.begin(), B.end(), mycmp);
	sort(C.begin(), C.end(), mycmp);
	sort(D.begin(), D.end(), mycmp);

	cout << A.size() + B.size() + C.size() + D.size()<<endl;
	//cout << A_num + B_num + C_num + D_num << endl;
	
	
	vector<model>::iterator i;
	for (i = A.begin(); i != A.end(); i++)
		printf("%d %d %d\n", (*i).id, (*i).score1, (*i).score2);

	for (i = B.begin(); i != B.end(); i++)
		//cout << (*i).id << " " << (*i).score1 << " " << (*i).score2 << endl;
		printf("%d %d %d\n", (*i).id, (*i).score1, (*i).score2);

	for (i = C.begin(); i != C.end(); i++)
		//cout << (*i).id << " " << (*i).score1 << " " << (*i).score2 << endl;
		printf("%d %d %d\n", (*i).id, (*i).score1, (*i).score2);

	for (i = D.begin(); i != D.end(); i++)
		printf("%d %d %d\n", (*i).id, (*i).score1, (*i).score2);
		//cout << (*i).id << " " << (*i).score1 << " " << (*i).score2 << endl;
	
	/*
	for (int i = 0; i < A_num; i++)
		cout << A[i].id << " " << A[i].score1 << " " << A[i].score2 << endl;
	for (int i = 0; i < B_num; i++)
		cout << B[i].id << " " << B[i].score1 << " " << B[i].score2 << endl;
	for (int i = 0; i < C_num; i++)
		cout << C[i].id << " " << C[i].score1 << " " << C[i].score2 << endl;
	for (int i = 0; i < D_num; i++)
		cout << D[i].id << " " << D[i].score1 << " " << D[i].score2 << endl;
		*/
	return 0;
}