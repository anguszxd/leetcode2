#coding:utf-8
#Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C 
#where the candidate numbers sums to T.

#The same repeated number may be chosen from C unlimited number of times.

#Note:
#All numbers (including target) will be positive integers.
#Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#The solution set must not contain duplicate combinations.
#For example, given candidate set 2,3,6,7 and target 7, 
#A solution set is: 
#[7] 
#[2, 2, 3] 


def combinationAll(s,t,ans,branch):
	if sum(branch) == t:
		branch = sort(branch)
		if branch not in ans:
			ans.append(branch)
		return
	if len(s) == 0 or sum(branch) > t:
		return
	comb = []

	#得到小于target的candidate numbers的组合的集合comb
	for i in range(1,len(s)+1,1):
		path = []
		combination(comb,path,i,s,t)
	
	if len(comb) == 0:
		return

	for i in range(len(comb)):
		combinationAll(s,t,ans,branch+comb[i])


def combination(res, path, n, sleft,target):
	if len(sleft) < n or sum(path) > target:
		return
	if n == 0 or len(sleft) == 0:
		res.append(path)
		return

	combination(res,path+[sleft[0]],n-1,sleft[1:],target)
	combination(res,path,n,sleft[1:],target)




def sort(subans):
	sort_res = []
#	subans.index(min(subans))
	for i in range(len(subans)):
		for j in range(0,len(subans)-1-i,1):
			if subans[j] > subans[j+1]:
				tmp = subans[j]
				subans[j] = subans[j+1]
				subans[j+1] = tmp
		#print subans
	return subans



can = [1,2,3,6,7]
t = 7
ans = []
branch = []
#print combinationSum(can,t)
combinationAll(can,t,ans,branch)
print ans