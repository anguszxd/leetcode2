#coding:utf-8
#Given an array and a value, remove all instances of that 
#value in place and return the new length.

#The order of elements can be changed. 
#It doesn't matter what you leave beyond the new length.

#仿照RemoveDuplicates，解决方法完全相同

def removeElem(nums,val):
	if nums == []:
		return 0

	j = 0

	for i in range(len(nums)):
		if nums[i] != val:
			nums[j] = nums[i]
			j += 1

	return j,nums

nums = [1,2,6,7,2,1,2,1,1,4,6,8,1]
leng,new = removeElem(nums,1)
print leng
print new