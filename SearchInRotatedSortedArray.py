#coding:utf-8

#Suppose a sorted array is rotated at some pivot unknown to you beforehand.

#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

#You are given a target value to search. If found in the array return its index, otherwise return -1.

#You may assume no duplicate exists in the array.

def search(nums, target):
	left = 0
	right = len(nums)-1

	while left < right:
		mid = (left + right) / 2
		if nums[mid] == target:
			return mid
		if nums[left] > nums[mid]:
			if target > nums[mid]:
				if target > nums[right]:
					right = mid-1
				else:
					left = mid+1
			else:
				right = mid-1
		else:
			if target > nums[mid]:
				left = mid+1
			else:
				if target > nums[right]:
					right = mid-1
				else:
					left = mid+1

	return -1

def SearchIndex(nums,target):
	if len(nums) == 0:
		return -1

	l, r = 0, len(nums)-1

	while l <= r:
		m = (l+r)>>1

		if target == nums[m]:
			return m
		if nums[m] < nums[r]:
			if target <= nums[r] and target > nums[m]:
				l = m+1
			else:
				r = m-1

		else:
			if target >= nums[l] and target < nums[m]:
				r = m-1
			else:
				l = m+1

	return -1

nums = [4,5,6,7,0,1,2]
target = 0
print SearchIndex(nums, target)