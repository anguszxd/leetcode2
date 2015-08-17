#coding:utf-8

#用二分法查找元素在序列中的位置

def binarySearch(nums,target):
	left, right = 0, len(nums)-1

	while left < right:
		mid = (left + right) >> 1

		if target > nums[mid]:
			left = mid + 1
		elif target < nums[mid]:
			right = mid - 1
		else:
			return mid
		print left,right

	return -1


nums = [0,1,2,3,5,6,7,8]
target = 9
print binarySearch(nums,target)