#coding:utf-8

#Given a sorted array, remove the duplicates in place such that 
#each element appear only once and return the new length.

#Do not allocate extra space for another array, 
#you must do this in place with constant memory.

#For example,
#Given input array nums = [1,1,2],

#Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
#It doesn't matter what you leave beyond the new length.

#pop重复的元素，使留下的元素都只出现一次
#leetcode AC但速度不快
def removeDuplicates(nums):
	if nums == []:
		return 0

	length = 1

	i = 0
	passnums = 1
	leng = len(nums)
	while passnums <= leng-1:
		passnums += 1
		if nums[i] == nums[i+1]:
			nums.pop(i+1)
		else:
			i += 1
			length += 1

	return length,nums

#该方法不pop出重复元素，遇到新的元素直接占用原数组中下一个位置
#因为题目中说超过返回长度部分不管
def removeDuplicates2(nums):
	if nums == []:
		return 0

	j = 1
	for i in range(len(nums)-1):
		if nums[i] != nums[i+1]:
			nums[j] = nums[i+1]
			j += 1
	return j,nums

nums = [1,1,1,2,3,4,4,5,6,6,6,7,7,7,7]
leng,newnums = removeDuplicates2(nums)
print leng
print nums