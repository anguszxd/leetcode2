#coding:utf-8

#Given an unsorted integer array, find the first missing positive integer.

#For example,
#Given [1,2,0] return 3,
#and [3,4,-1,1] return 2.

#Your algorithm should run in O(n) time and uses constant space

#注意这题的意思，给定的数组中有可能有重复的数字的，比如[1,1]
#Solution1:不断交换元素位置，使其能满足：nums[i] == i+1
#经过交换，数字前面一段的位置会符合nums[i] == i+1的要求
#即被正整数元素占据，其他元素，如非整数和多余的正数会被甩到数组的后半段
#完成以上交换后，再遍历整个数组，找到第一个不符合nums[i] == i+1的元素的位置
#答案就是i+1
def firstMissingPositive(nums):
	if len(nums) == 0:
		return 1

	i = 0
	while i < len(nums):
		if nums[i] > 0 and nums[i] != i+1 and nums[i] < len(nums) and nums[i] != nums[nums[i]-1]:
			tmp = nums[i]
			nums[i] = nums[nums[i]-1]
			nums[tmp-1] = tmp
		else:
			i += 1
	
	for i in range(len(nums)):
		if nums[i] != i+1:
			return i+1

	return len(nums)+1

n = [1,1]
print firstMissingPositive(n)