// LongestSubstring.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

int lengthOfLongestSubstring(string s) {
         int locs[256];//�����ַ���һ�γ��ֵ�λ��
        memset(locs, -1, sizeof(locs));

        int idx = -1, max = 0;//idxΪ��ǰ�Ӵ��Ŀ�ʼλ��-1
        for (int i = 0; i < s.size(); i++)
        {
			//cout<<s[i]<<endl;
            if (locs[s[i]] > idx)//�����ǰ�ַ����ֹ�����ô��ǰ�Ӵ�����ʼλ��Ϊ����ַ���һ�γ��ֵ�λ��+1
				//C++�������±������char�ͱ���
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

