#coding:utf-8
#Given n pairs of parentheses, write a function to generate 
#all combinations of well-formed parentheses.

#For example, given n = 3, a solution set is:

#"((()))", "(()())", "(())()", "()(())", "()()()"

#Solution：括号配对的问题相当于是进栈出栈的操作，即有n个元素，找出其所有进栈出栈的方式
#可以用树结构分析
#控制数的深度与结构：left：表示左边还有多少个"("没有配对；LeftNum：表示左边已经有多少个"("
	#结束条件：LeftNum == n
def generateParenthesis(n):
	res = []
	Path = ""
	BracketMatching(res, 0, Path, 0, n)
	return res

def BracketMatching(res, left, path, LeftNum, n):
	#当前分支结束条件，LeftNum == n
	#在结果上加上一种情况(path)
	if LeftNum == n:
		for i in range(left):
			path += ")"
		res.append(path)
		return

	#左边没有"("未配对，加"(",修改left+1，LeftNum+1
	if left == 0:
		BracketMatching(res, left+1, path+"(", LeftNum+1, n)
	else:
	#如果左边还有"("为配对，有两种选择：1.加"(";2.加")"与一个"("配对
	#修改相应的left和LeftNum
		BracketMatching(res, left+1, path+"(", LeftNum+1, n)
		BracketMatching(res, left-1, path+")", LeftNum, n)




n = 1
print generateParenthesis(n)