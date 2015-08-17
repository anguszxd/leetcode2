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



S = [8,5,12,3,-2,-13,-8,-9,-8,10,-10,-10,-14,-5,-1,-8,-7,-12,4,4,10,-8,0,-3,4,11,-9,-2,-7,-2,3,-14,-12,1,-4,-6,3,3,0,2,-9,-2,7,-8,0,14,-1,8,-13,10,-11,4,-13,-4,-14,-1,-8,-7,12,-8,6,0,-15,2,8,-4,11,-4,-15,-12,5,-9,1,-2,-10,-14,-11,4,1,13,-1,-3,3,-7,9,-4,7,8,4,4,8,-12,12,8,5,5,12,-7,9,4,-12,-1,2,5,4,7,-2,8,-12,-15,-1,2,-11]
print threeSum3(S)
#print sort(S)