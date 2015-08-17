#coding:utf-8

def findMini(nums):
	left = 0
	right = len(nums)-1
	mid = left

	while nums[left] >= nums[right]:
		if right-left == 1:
			mid = right
			break

		mid = (left+right)>>1
		if nums[mid] >= nums[left]:
			left = mid
		elif nums[mid] <= nums[right]:
			right = mid

	return mid


n = [7,8,9,10,11,12,0,1,2,3,4,5,6]
print findMini(n)