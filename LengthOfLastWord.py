#coding:utf-8

#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

#If the last word does not exist, return 0.

#Note: A word is defined as a character sequence consists of non-space characters only.

#For example, 
#Given s = "Hello World",
#return 5.

#这题比较简单，求最后一个单词长度只需要从字符串末尾开始计数就可以了
#需要注意的特殊情况：1、字符串是空串，直接返回0
#2、字符串末尾有空格，如"a   "，末尾的空格要省略
def lengthOfLastWord(s):
	if len(s) == 0:
		return 0
	i = len(s) - 1
	leng = 0
	lastBegin = False
	while i >=0:
		#字符串末尾有空格时，要跳过这些空格再计数
		if s[i] != ' ':
			lastBegin = True
		if lastBegin:
			if s[i] == ' ':
				break
			leng += 1
		i -= 1
			

	return leng


s = "h   "
print lengthOfLastWord(s)