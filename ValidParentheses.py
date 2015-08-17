#coding:utf-8
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
#determine if the input string is valid.

#The brackets must close in the correct order, 
#"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

#遇到({[相当于是进栈操作，压入栈中
#遇到)}]相当于是出栈操作，将栈顶元素弹出，查看弹出的和当前元素是否配对

#注意一些特殊情况，如输入字符串为空，应当认为是正确的
#如果最后栈不为空，表示还有元素没有配对，应当认为是错误的

def isValid(s):
	stack = []
#构建一个字典，存储配对的元素，用于判断是否配对成功
	d = {'{':'}','[':']','(':')'}
	isVa = True
#这个if判断可以不要，s为空时，会跳过for循环，直接输出isVa
#	if s == '':
#		return isVa

	for i in range(len(s)):
		#if s[i] == "(" or s[i] == "{" or s[i] == "[":
		if s[i] in d:
			stack.append(s[i])
		else:
			if stack==[]:
				isVa = False
				break
			elempop = stack.pop()
			if s[i] != d[elempop]:
				isVa = False
				break
	if stack != []:
		isVa = False
	return isVa

s='['
print isValid(s)