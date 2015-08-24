#coding:utf-8

#Given an array of non-negative integers, you are initially positioned at the first index of the array.

#Each element in the array represents your maximum jump length at that position.

#Your goal is to reach the last index in the minimum number of jumps.

#For example:
#Given array A = [2,3,1,1,4]

#The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

def jump(n):
	minlen = len(n)
	curlen = 0
	minlen = helper(n,minlen,curlen)
	return minlen

def helper(n,minlen,curlen):
	if len(n) == 1:
		return curlen

	oneintail = 0
	for i in range(len(n)-2,-1,-1):
		if n[i] == 1:
			oneintail += 1
		else:
			break
	
	reach = reachable(n)


	for i in range(len(reach)):
		if n[reach[i]] == 1:
			curlen = helper(n[0:-oneintail],minlen,curlen+oneintail)
		else:
			curlen = helper(n[0:reach[i]+1],minlen,curlen+1)
		if curlen < minlen:
			minlen = curlen
		else:
			break

	return minlen

def reachable(n):
	reachindex = []
	leng = len(n)
	for i in range(leng-1):
		if n[i]+i >= leng-1:
			reachindex.append(i)
	return reachindex

A = [1,2,1,1,1]
print jump(A)