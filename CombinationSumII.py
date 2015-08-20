#coding:utf-8

#Given a collection of candidate numbers (C) and a target number (T), 
#find all unique combinations in C where the candidate numbers sums to T.

#Each number in C may only be used once in the combination.

def combinationSum(c,t,ans,path):
	if sum(path) == t:
		if path not in ans:
			ans.append(path)
		return False
	if sum(path) > t:
		return False

	for i in range(1,len(c),1):
		flag = combinationSum(c[i:],t,ans,path+[c[i-1]])
		if not flag:
			break

	return True


nums = [1,2]
target = 1
nums.sort()

ans = []
path = []

combinationSum(nums,target,ans,path)
print ans