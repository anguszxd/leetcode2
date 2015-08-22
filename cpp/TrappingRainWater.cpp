#include <iostream>
#include <vector>

template <class T>
int getArrayLen(T& array)
{
return (sizeof(array) / sizeof(array[0]));
}

int trap(int* height, int n)
{
	int l = 0, r = n-1, level = 0, water=0;
	while(l < r)
	{
		//比较左右两边的大小，较大那个相当于是挡板，容量看较小的一边
		int lower = height[height[l] < height[r] ? l++:r--];
		level = level > lower ? level : lower;
		water += level-lower;
		std::cout << level << lower << water << std::endl;
	}
	return water;
}

int main()
{
	int h[] = {4,2,0,3,2,5};
	int n = getArrayLen(h);

	int water = trap (h,n);

	std::cout << water << std::endl;
	return 0;
}