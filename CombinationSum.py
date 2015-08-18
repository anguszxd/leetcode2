#coding:utf-8
#Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

#The same repeated number may be chosen from C unlimited number of times.

#Note:
#All numbers (including target) will be positive integers.
#Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#The solution set must not contain duplicate combinations.
#For example, given candidate set 2,3,6,7 and target 7, 
#A solution set is: 
#[7] 
#[2, 2, 3] 


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


def combinationSum(candidates,target):



can = [2,3,6,7]
t = 7
print combinationSum(can,t)