#include <iostream>
#include <math.h>
using namespace std;
bool prime(int i){
	for(int j=2; j<=sqrt(i); j+=1){
		if(i%j==0) return false;
	}
	return true;
}

int main(){
	int start, end;
	int index = 1;
	int cur = 2;
	int i = 3;
	cin>>start>>end;
	if(start == 1){
		if(end>start)
			cout<<"2 ";
		else cout<<"2";
		index++;
	}

	while(cur <= end){
		if(prime(i)){
			if(cur == end){
				cout<<i;
				index++;
			}
			else if(cur >= start){
				if(index%10==0)
					cout<<i<<endl;
				else cout<<i<<" ";
				index++;
			}
			cur++;
		}
		i+=2;
	}
	return 0;
}
