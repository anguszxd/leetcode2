#coding:utf-8
#方法一：推算出每个位置坐标在新序列中的表达式
#该方法在leetcode中超时了
def convert(s,nRows):
	if nRows <= 1 or len(s)==0:
		return s

	res = ''
	ls = len(s)
	for i in range(0,nRows):
		if i>ls:
			break

		idx = i
		res += s[idx]

		for k in range(1,ls):
			if i==0 or i == nRows-1:
				idx += 2*nRows-2
			else:
				if k & 0x1:
					idx += 2*(nRows-1-i)
				else:
					idx += 2*i

			if(idx<ls):
				res += s[idx]

	return res

#利用Z字形排列的特点，将所有字符划分到nRows个tmp子串中
#第0个子串放置原第0行字符，依次类推
#因此，只需确定字符放置在哪个tmp子串中就行了
#利用step加减tmp号，从上往下走是step=1，从下往上走step=-1
#方向改变条件：index==nRows时，从往下走变为往上走
#index==-1时，从往上走变成往下走
#时间复杂度O(n)
def convert2(s, nRows):
	if nRows==1: return s
	tmp=['' for i in range(nRows)]
	index=-1; step=1
	for i in range(len(s)):
		index += step
		if index==nRows:
			index -= 2; step=-1
		elif index==-1:
			index=1; step=1
		tmp[index] += s[i]
	return ''.join(tmp)


s="ABCDEFGHIJKLM"
print len(s)
s_convert = convert2(s,4)
print s_convert
print len(s_convert)