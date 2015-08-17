#coding:utf-8

#输出字符串中字符的所有组合情况，
#如输入"abc"，输出：a,b,c,ab,bc,ac,abc

#s是输入字符串，n是s中参与组合的字符数量
def combinationAll(s):
	res = []

	for i in range(1,len(s)+1,1):
		path = ""
		combination(res,path,i,s)
	print res

def combination(res, path, n, sleft):
	if len(sleft) < n:
		return
	if n == 0 or len(sleft) == 0:
		res.append(path)
		return

	combination(res,path+sleft[0],n-1,sleft[1:])
	combination(res,path,n,sleft[1:])


s = "abcd"
combinationAll(s)