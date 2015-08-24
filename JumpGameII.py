#coding:utf-8

#Given an array of non-negative integers, you are initially positioned at the first index of the array.

#Each element in the array represents your maximum jump length at that position.

#Your goal is to reach the last index in the minimum number of jumps.

#For example:
#Given array A = [2,3,1,1,4]

#The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

#Solution1:自己想的方法，从最后开始反向寻找能达到队尾的位置有哪些，
#将队列尾部的元素去掉，递归搜索，跳数加1 ，直到找到队伍的第一个元素，
#输出所有可能结果中最小的长度。
#以上思路没有问题，但使用了递归，效率不高，而且当输入的序列是很多连续的1时，可能出现递归层数不够用的情况
def jump(n):
	minlen = len(n)
	curlen = 0
	minlen = helper(n,minlen,curlen)
	return minlen

def helper(n,minlen,curlen):
	if len(n) == 1:
		return curlen

	reach = reachable(n)

	for i in range(len(reach)):
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

#Solution2:使用了贪婪算法，让每一跳能够达到最远的位置
#last记录上一跳能到达的最远的位置，curr是这一跳能到达的最远位置
#从0开始遍历整个序列，当i>last还没结束循环，意味着跳数要+1，而且
#last更新为curr
def jumpGreedy(n):
	ret, last, curr = 0, 0, 0
	for i in range(len(n)):
		if i > curr:
			return -1
		if i > last:
			last = curr
			ret += 1
		curr = max(curr, i+n[i])

	return ret


A = [2,3,1,1,4]
print jumpGreedy(A)