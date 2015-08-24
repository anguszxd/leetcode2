#include <iostream>
using namespace std;

int list(int A[], int n){
	int *d = new int[n];
	int len = 1;
	for(int i=0; i<n; i++){
		d[i] = 1;
		for(int j=0; j<i; j++)
			if(A[j]<=A[i] && d[j]+1>d[i])
				d[i] = d[j]+1;
		if(d[i]>len) len = d[i];
	}
	delete[] d;
	return len;
}

int main(){
	int A[] = {2,1,5,3,6,4,8,9,7};

	cout<<list(A,9)<<endl;
	return 0;
}