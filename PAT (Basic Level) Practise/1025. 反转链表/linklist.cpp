#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <map>

using namespace std;

class Node{
public:
	int addr;
	int data;
	int next;
};

int main()
{
	int start, N, K;
	scanf("%d %d %d", &start, &N, &K);
	map<int, Node> linklist;
	for (int i = 0; i < N; i++){
		int addr, data, next;
		scanf("%d %d %d", &addr, &data, &next);
		Node cur;
		cur.addr = addr;
		cur.data = data;
		cur.next = next;
		linklist[addr] = cur;
	}
	int cur_addr = start;
	N = 0;
	while (cur_addr != -1){
		cur_addr = linklist[cur_addr].next;
		N++;
	}
	cur_addr = start;
	int i;
	for (i = 0; i+K-1 < N; i += K){
		Node *Node_tmp = new Node[K];
		for (int j = 0; j < K; j++){
			Node_tmp[j] = linklist[cur_addr];
			cur_addr = Node_tmp[j].next;
		}
		
		int next_start = Node_tmp[K - 1].next;
		if ((i+K+K-1)<N){
			for (int k = 0; k<K-1; k++)
				next_start = linklist[next_start].next;
		}
		Node_tmp[0].next = next_start;
		for (int j = K-1; j > 0; j--){
			Node_tmp[j].next = Node_tmp[j-1].addr;
		}
		for (int j = K-1; j >= 0; j--){
			if (Node_tmp[j].next != -1)
				printf("%05d %d %05d\n", Node_tmp[j].addr, Node_tmp[j].data, Node_tmp[j].next);
			else
				printf("%05d %d %d\n", Node_tmp[j].addr, Node_tmp[j].data, Node_tmp[j].next);
		}
		delete[] Node_tmp;
	}

	while (cur_addr != -1 && i!=N){
		if (linklist[cur_addr].next != -1)
			printf("%05d %d %05d\n", linklist[cur_addr].addr, linklist[cur_addr].data, linklist[cur_addr].next);
		else
			printf("%05d %d %d\n", linklist[cur_addr].addr, linklist[cur_addr].data, linklist[cur_addr].next);
		cur_addr = linklist[cur_addr].next;
	}

	return 0;
}