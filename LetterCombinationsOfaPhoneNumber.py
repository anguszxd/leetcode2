#coding:utf-8
#Given a digit string, return all possible letter combinations that the number could represent.

#Input:Digit string "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

#Solution1:本题是组合的问题，如输入"23"，输出有3X3种组合
#所以，输入字符串每加一个字符，就要将原来的输出结果数量扩大n倍，n是添加数字字符对应的字母数量
def letterCombinations(digits):
	
	mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
	res = []
	if digits == "":
		return res

	res = list(mapping[digits[0]])
	for i in range(1,len(digits)):
		#复制res，扩大res结果数量
		res *= len(mapping[digits[i]])
		s = mapping[digits[i]]
		fr = len(res)/len(s)
		for j in range(len(res)):
			#res[j] += s[j/(len(res)/len(s))]
			res[j] += s[j/fr]

	return res

#Solution2：用递归函数
def letterCombinations2(digits):
    if not digits:
        return []
    dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    res = []
    dfs(digits, dic, 0, "", res)
    return res

def dfs(digits, dic, index, path, res):
    if len(path) == len(digits):
        res.append(path)
        return 
    for i in xrange(index, len(digits)):
        for j in dic[digits[i]]:
            dfs(digits, dic, i+1, path+j, res)

digits = "23"

print letterCombinations2(digits)