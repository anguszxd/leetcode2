#coding:utf-8

#Given a sorted array and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

#You may assume no duplicates in the array.

#Here are few examples.
#[1,3,5,6], 5 → 2
#[1,3,5,6], 2 → 1
#[1,3,5,6], 7 → 4
#[1,3,5,6], 0 → 0

#原理还是二分法，由于target可能不在数组中，要返回其可能的位置
#使用二分法会不断接近target应该在的位置，当target不在数组中时，
#left、right指针的变动会使得搜索段直接跳过target
#因此要找到target所在的位置需要注意指针变动的情况
def searchInsert(nums, target):
	left, right = 0, len(nums)-1

	if target < nums[0]: return 0
	if target > nums[-1]: return len(nums)

	while left <= right:
		mid = (left + right) >> 1

		if target > nums[mid]:
			#mid指针变动使得搜索段跳过target，
			#这就表示target在mid后mid+1之前
			if target < nums[mid+1]:
				return mid+1
			left = mid + 1
		elif target < nums[mid]:
			if target > nums[mid-1]:
				return mid
			right = mid - 1
		else:
			return mid
		


nums = [1]
target = 0

print searchInsert(nums,target)