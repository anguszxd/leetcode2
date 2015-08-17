#coding:utf-8
#罗马数字书写规则：当前位比前一位大，则用当前位数字减去原数字
#当前位比前一位小，则加上当前位数字
#如XIV=14，最末位V肯定是加上的，因此初始化ans=val[s[-1]]
#再看前面几位，第0位X>第1位I，所以ans+=X
#第1位I<第2位V，所以ans-=I，最终结果14
def RomanToInt(s):
#生成dict，key:val
	val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

	ans = val[s[-1]]

	for i in range(len(s)-1):
		if val[s[i]] < val[s[i+1]]:
			ans -= val[s[i]]
		else:
			ans += val[s[i]]

	return ans


s='XIV'
print RomanToInt(s)