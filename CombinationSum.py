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


#Solution1:用找组合的方式逐步寻找符合要求的结果
#找到的组合应该是所有小于等于target的候选数字的组合
#如candidate set [2,3,6,7]，target=7
#第一次找到的组合是:[[2],[3],[2,3],[7]]
#只有在这些组合的基础上才可能出现满足要求的结果
#下一步是在某个组合的基础上继续上面的过程，
#如取[2]，继续在原来的优选数字中找组合加到[2]上，使其满足小于等于target
#第二次搜索的结果是：[[2,2],[2,3]]
#以上是迭代的过程，退出条件：1组合求和正好等于target，加入到ans中（如果原先ans中没有这个答案的话）
#2继续找下去满足加和小于等于target的组合的数量为0
def combinationSum(s,t,ans,branch):
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


#Solution2:以上方法思路没有问题，但计算组合是没有必要的，可以使用溯回法退回，
#回溯法：先对候选数字排序，不断找可能的组合，即组合的加和小于target，继续从小到大添加候选数字
#直到遇到组合的加和等于target，将组合加入ans并返回
#或者加和大于target，返回，这条路径后面的搜索也就不必要了

def combinationSum2(s,t,path,ans,start):
	if sum(path) == t:
		#path = sort(path)
		#if path not in ans: ans.append(path)
		ans.append(path)
		return False
	if sum(path) > t:
		return False

	for i in range(start,len(s),1):
		flag = combinationSum2(s,t,path+[s[i]],ans,i)
		if not flag: break
	return True

can = [1,2,3,6,7]
t = 7
ans = []
path = []
#print combinationSum(can,t)
combinationSum2(can,t,path,ans,0)
print ans