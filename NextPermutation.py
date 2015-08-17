#coding:utf-8
#Implement next permutation, which rearranges numbers into the lexicographically 
#next greater permutation of numbers.

#If such arrangement is not possible, it must rearrange it as the lowest possible order 
#(ie, sorted in ascending order).

#The replacement must be in-place, do not allocate extra memory.

#Here are some examples. Inputs are in the left-hand column and its corresponding outputs are 
#in the right-hand column.
#1,2,3 → 1,3,2
#3,2,1 → 1,2,3
#1,1,5 → 1,5,1

#字符集{1,2,3}的字典序，数字较小的优先：
#123,132,213,231,312,321

#字符集{1,2,3,4}的字典序：
#1234,1243,1324,1342,1423,1432,
#2134,2143,2314,2341,2413,2431,
#3124,3142,3214,3241,3412,3421,
#4123,4132,4213,4231,4312,4321.

def nextPermutation(nums):
	#找到最后一个升序位置pos，从后往前找
	pos = -1
	for i in range(len(nums)-1,0,-1):
		if nums[i] > nums[i-1]:
			pos = i - 1
			break

	#不存在升序，即整个数列是降序排列的
	if pos < 0:
		nums = reverse(nums, 0, len(nums)-1)
		return nums

	#若存在升序，找到pos之后最后一个比它大的位置
	#交换位置
	for  i in range(len(nums)-1,pos,-1):
		if nums[i] > nums[pos]:
			tmp = nums[i]
			nums[i] = nums[pos]
			nums[pos] = tmp
			break

	#反排pos之后的数
	nums = reverse(nums,pos+1,len(nums)-1)

	return nums


def reverse(nums,begin,end):
	l, r = begin, end

	while l < r:
		tmp = nums[l]
		nums[l] = nums[r]
		nums[r] = tmp

		l += 1
		r -= 1

	return nums

nums = [3,1,2,4]
print nextPermutation(nums)