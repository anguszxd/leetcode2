#coding:utf-8

#Given a sorted array of integers, find the starting and ending position of a given target value.

#Your algorithm's runtime complexity must be in the order of O(log n).

#If the target is not found in the array, return [-1, -1].

#For example,
#Given [5, 7, 7, 8, 8, 10] and target value 8,
#return [3, 4]

#Solution：先用二分法找到一个target，再由这个位置出发向左右两端寻找第一个不是
#target的位置
def searchRange(nums,target):
	l, r = 0, len(nums)-1

	while l <= r:
		m = (l+r)>>1
		if nums[m] == target:
			break
		if nums[m] > target:
			r = m-1
		else:
			l = m+1
			
	if nums[m] != target:
		return [-1,-1]
	
	start = m
	end = m
	while start != 0:
		if nums[start-1] == target:
			start -= 1
		else:
			break

	while end != len(nums)-1:
		if nums[end+1] == target:
			end += 1
		else:
			break

	res = [start, end]

	return res


nums = [0,1,2,3,4,5,9]
target = 1
print searchRange(nums,target)