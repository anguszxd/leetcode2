#coding:utf-8
#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero.

#Note:
#Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
#The solution set must not contain duplicate triplets.

#Solution1:可以将3Sum问题转化为2Sum问题，如取nums[i]做测试，
#则将除nums[i]外的元素组成新的数列，而目标变成target-nums[i],在新数列中寻找新目标
#即转化为2Sum问题，本题中target=0
#找到符合要求的一组数后（3个数一组），再进行排序查重等
#该方法效率不高，leetcode上out of time
def threeSum(nums):
	target = 0
	res = []
	for i in range(len(nums)):
		tmparray = nums
		checknum = tmparray[i]
		tmptarget = target - checknum
		tmparray.pop(i)
		#print tmparray
		process = {}
		for j in range(len(tmparray)):
			if tmptarget-tmparray[j] in process:
				subans = sort([checknum,tmparray[j],tmptarget-tmparray[j]])
				if subans not in res: res.append(subans)
			process[tmparray[j]] = j

		nums.insert(i,checknum)

	return res


def threeSum3(nums):
	target = 0
	nums = sort(nums)
	res = []
	for i in range(len(nums)):
		tmparray = nums
		checknum = tmparray[i]
		tmptarget = target - checknum
		tmparray.pop(i)
		#print tmparray
		process = {}
		for j in range(len(tmparray)):
			if tmptarget-tmparray[j] in process:
				subans = [checknum,tmparray[j],tmptarget-tmparray[j]]
				if subans not in res: res.append(subans)
			process[tmparray[j]] = j

		nums.insert(i,checknum)

	return res



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

def threeSum2(nums):
	target = 0
	nums = sort(nums)
	above, below = [], []
	res = []
	for i in range(len(nums)):
		if nums[i] > 0:
			above.append(nums[i])
		else:
			below.append(nums[i])

	#print above
	#print below

	for i in range(len(above)):
		tmptarget = - above[i]
		process = {}
		for j in range(len(below)):
			if tmptarget-below[j] in process:
				#subans = sort([checknum,tmparray[j],tmptarget-tmparray[j]])
				subans = [tmptarget-below[j],below[j],above[i]]
				if subans not in res: res.append(subans)
				#res.append(subans)
			process[below[j]] = j

	for m in range(len(below)):
		tmptarget = - below[m]
		process = {}
		for n in range(len(above)):
			if tmptarget - above[n] in process:
				subans = [below[m],above[n],tmptarget-above[n]]
				if subans not in res: res.append(subans)

			process[above[n]] = n
	return res

def twoSum(num, target):
    process={}
    for index in range(len(num)):
        print process
        if target-num[index] in process:
            return [process[target-num[index]]+1,index+1]
        process[num[index]]=index


#先找到数组的所有三元素的组合，再对这些组合进行检查，看是否满足和为0
#很容易理解，但效率较低，在OJ中超时
def CombinatinThreeSum(nums):
	comb = []
	path = []
	res = []
	nums = sort(nums)
	combination(comb,path,3,nums)
	for i in range(len(comb)):
		if sum(comb[i])==0 and comb[i] not in res:
			res.append(comb[i])

	return res


def combination(res, path, n, sleft):
	if len(sleft) < n:
		return
	if n == 0 or len(sleft) == 0:
		res.append(path)
		return

	combination(res,path+[sleft[0]],n-1,sleft[1:])
	combination(res,path,n,sleft[1:])


S = [8,5,12,3,-2,-13,-8,-9,-8,10,-10,-10,-14,-5,-1,-8,-7,-12,4,4,10,-8,0,-3,4,11,-9,-2,-7,-2,3,-14,-12,1,-4,-6,3,3,0,2,-9,-2,7,-8,0,14,-1,8,-13,10,-11,4,-13,-4,-14,-1,-8,-7,12,-8,6,0,-15,2,8,-4,11,-4,-15,-12,5,-9,1,-2,-10,-14,-11,4,1,13,-1,-3,3,-7,9,-4,7,8,4,4,8,-12,12,8,5,5,12,-7,9,4,-12,-1,2,5,4,7,-2,8,-12,-15,-1,2,-11]
#S = [-2,-1,-1,0,0,0,2]
n = [-13,11,11,0,-5,-14,12,-11,-11,-14,-3,0,-3,12,-1,-9,-5,-13,9,-7,-2,9,-1,4,-6,-13,-7,10,10,9,7,13,5,4,-2,7,5,-13,11,10,-12,-14,-5,-8,13,2,-2,-14,4,-8,-6,-13,9,8,6,10,2,6,5,-10,0,-11,-12,12,8,-7,-4,-9,-13,-7,8,12,-14,10,-10,14,-3,3,-15,-14,3,-14,10,-11,1,1,14,-11,14,4,-6,-1,0,-11,-12,-14,-11,0,14,-9,0,7,-12,1,-6]
print CombinatinThreeSum(n)
#print threeSum3(S)
#print sort(S)