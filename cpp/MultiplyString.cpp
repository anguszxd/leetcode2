
#include <string.h>
#include <iostream>
#include <math.h>

using namespace std;
/*
// 先将字符串转化成数字，对数字做乘法，再将数字转换成字符串
//当两个乘数较小时是有效的，但当乘数很大时，结果会溢出(用long long型都不够长)
//所以要用别的方法
int main()
{
	string num1 = "123456789";
	string num2 = "987654321";

	int len1 = num1.size();
	int len2 = num2.size();

	long long n1 = 0;
	long long n2 = 0;

	for(int i=0;i<len1;i++)
		n1 += (num1[i] - '0')*pow(10,len1-i-1);
	for(int i=0;i<len2;i++)
		n2 += (num2[i] - '0')*pow(10,len2-i-1);

	long long res = n1*n2;

	string ss = "";
	while(res != 0)
	{
		ss = char(res%10+'0')+ss;
		res /= 10;
	}


	cout << ss << endl;
	return 0;
}
*/

//模拟手写计算过程
int main()
{
	string num1 = "14";
	string num2 = "23";

	int len1 = num1.size();
	int len2 = num2.size();

	int *n1 = new int[len1];
	int *n2 = new int[len2];
	int *res = new int[len1+len2];
	//表示res开始的内存块都设为0
	memset(res, 0, sizeof(int)*(len1+len2));

	for(int i=0;i<len1;i++)
		//n1 += (num1[i] - '0')*pow(10,len1-i-1);
		n1[i] = num1[i] - '0';
	for(int i=0;i<len2;i++)
		n2[i] = num2[i] - '0'; 

	for(int i=0;i<len1;i++)
		for(int j=0;j<len2;j++)
			res[i+j+1] += n1[i]*n2[j];
	string ss = "";
	
	for(int k = len1+len2-1;k>=0;k--)
	{
		if(k>0)
			res[k-1] += res[k]/10;
		res[k] %= 10;
		ss = char(res[k]+'0')+ss;
	}
	ss = ss[0]=='0'?ss.substr(1):ss;
	cout << ss << endl;
	return 0;
}