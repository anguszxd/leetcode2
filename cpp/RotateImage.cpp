#include <vector>
#include <iostream>

using namespace std;

void helper(vector<vector<int> >&matrix, int start);
void rotate(vector<vector<int> >& matrix);

int main(){
	vector<vector<int> > matrix;
	int n = 0;
	cin >> n;
	//initalize the matrix
	matrix.resize(n);
	for(int i=0; i<n; i++)
	{
		matrix[i].resize(n);
		for(int j=0; j<n; j++)
		{
			matrix[i][j] = i*n+j+1;
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
	rotate(matrix);
	cout << "after rotate:" << endl;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<n; j++)
		{
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}

void rotate(vector<vector<int> >& matrix){
	int n = matrix.size();
	for(int i=0; i<n/2; i++)
	{
		helper(matrix, i);
	}
}

void helper(vector<vector<int> >&matrix, int start){
	int n = matrix.size();
	for(int i = start; i<n-1-start; i++)
	{
		int tmp1 = matrix[n-1-i][start];
		int tmp2 = matrix[start][i];
		int tmp3 = matrix[i][n-1-start];
		int tmp4 = matrix[n-start-1][n-1-i];
		matrix[start][i] = tmp1;
		matrix[i][n-1-start] = tmp2;
		matrix[n-start-1][n-1-i] = tmp3;
		matrix[n-1-i][start] = tmp4;
	}
}