#include <iostream>

double myPow(double x, int n);

int main(){
	double x = 0.0;
	int n = 0;

	std::cout << "input x:" << std::endl;
	std::cin >> x;
	std::cout << "input n:" << std::endl;
	std::cin >> n;

	std::cout << "answer is: " << myPow(x, n) <<std::endl;

	return 0;
}

double myPow(double x, int n)
{
	if(n < 0)
	{
		x = 1/x;
		n = -n;
	}

	double ans = 1.0;
	double cur = x;

	while( n>0 )
	{
		if(n&0x1)
			ans *= cur;
		cur *= cur;
		n = n >> 1;
	}

	return ans;
}