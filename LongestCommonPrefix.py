#coding:utf-8
#查找出所有字符串的最长公共前缀

#方法一：取出每一个字符串最前面的字符，逐一比较，如果该位置上所有字符串的字符都相同，
#说明该字符是最长公共子串的一部分
#重复该过程直到出现不同或最短的字符串已经用完所有字符，结束
def longestCommonPrefix(strs):
	minLen = 1000
	#find the length of the shortest string
	for i in range(len(strs)):
		if len(strs[i]) < minLen:
			minLen = len(strs[i])

	longComPre = ''
#针对可能出现的特殊情况，如输入为空，要有特别的处理
#输入只有字符串数组只有一个字符串，也是一种特殊情况，返回该字符串就可以了
	if len(strs) == 0:
		return longComPre
	if len(strs) == 1:
		return strs[0]


	for i in range(minLen):
		curChar = strs[0][i]

		for j in range(1,len(strs)):
			if strs[j][i] == curChar:
				continue
			else:
				j -= 1
				break

		if j == len(strs)-1:
			longComPre += curChar
		else:
			break

	return longComPre

#运用分而治之的思想完成
#两个字符串的最大公共前缀一定不会超过最小那个字符串
#当字符串数组中只有一个字符串时，最大公共前缀就是其本身
#先将所有字符串不断的二分，直到字符串数组为空或只有一个
#再进行两两合并，获得这两个字符串的最长公共前缀，
#直到所有的字符串都完成了合并，得到所有字符串的最长公共子串

#分而治之的方法的优点在于，能将复杂的问题分解为简单的问题
#降低解决问题的复杂度
def longestCommonPrefix2(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
        #//双斜杠除法，用于浮点数除法，其结果进行四舍五入。
    h1 = longestCommonPrefix(strs[:len(strs)//2])
    h2 = longestCommonPrefix(strs[len(strs)//2:])
    return merge(h1, h2)

def merge(h1, h2):
    i = 0
    while i < len(h1) and i < len(h2) and h1[i] == h2[i]:
        i += 1
    return h1[:i]

strs = []
print longestCommonPrefix(strs)