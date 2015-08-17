#coding:utf-8

#输入字符串，输出该字符串中字符的所有排列，
#如输入abc，输出：abc,acb,bac,bca,cab,cba
#采用递归的方法得到的结果是按字典序排列的
def stringPermutation(s):
	res = []
	path = ""
	permutation(res,s,path)
	print res


def permutation(res, st, path):
	if len(st) == 1:
		res.append(path+st)
		return

	for i in range(len(st)):
		permutation(res,st[0:i]+st[i+1:],path+st[i])


s = "123456"
stringPermutation(s)