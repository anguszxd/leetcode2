// LongestSubstring.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

int lengthOfLongestSubstring(string s) {
         int locs[256];//保存字符上一次出现的位置
        memset(locs, -1, sizeof(locs));

        int idx = -1, max = 0;//idx为当前子串的开始位置-1
        for (int i = 0; i < s.size(); i++)
        {
			//cout<<s[i]<<endl;
            if (locs[s[i]] > idx)//如果当前字符出现过，那么当前子串的起始位置为这个字符上一次出现的位置+1
				//C++中数组下标可以是char型变量
            {
				//cout<<locs[s[i]]<<endl;
                idx = locs[s[i]];
            }

            if (i - idx > max)
            {
                max = i - idx;
            }

            locs[s[i]] = i;
        }
		for (int i = 0; i < s.size(); i++)
		{
			cout<<s[i]<<endl;
			cout<<locs[s[i]]<<endl;
		}
        return max;
    
        
    }

int _tmain(int argc, _TCHAR* argv[])
{
	string s="fabcabcabc";
	int length=lengthOfLongestSubstring(s);
	cout<<length<<endl;
	return 0;
}

