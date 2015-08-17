#coding:utf-8

#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#Note:
#You may assume that nums1 has enough space (size that is greater or equal to m + n) 
#to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


#Solution：两个array合并成一个，把nums2合并到nums1
#注意array存储方式是线性的，在array中插入元素很麻烦，因为要将后面的元素都往后移一位
#为解决array插入的问题，可以从后往前插入，这样就不需要移动后面的元素了
#这题要注意m和n并不是nums1和nums2的长度，而是nums1、nums2初始化的长度
def merge(nums1,m,nums2,n):
	if m == 0: 
		nums1[:] = nums2[:]
		return
	if n == 0:
		return

	#nums1 += [0]*n
	#nums1 = nums1[0:m] + [0]*n
	#nums1用于保存结果，先对其初始化，使其有足够的长度保存结果
	#注意如果nums1长度不够，要用append添加元素
	for i in range(m,m+n,1):
		if i >= len(nums1):
			nums1.append(0)
		else:
			nums1[i] = 0
	           
	i = m+n-1
	while m > 0 and n > 0:
	#for i in range(m+n-1,-1,1):
		if nums1[m-1] > nums2[n-1]:
			nums1[i] = nums1[m-1]
			m -= 1
		else:
			nums1[i] = nums2[n-1]
			n -= 1
		i -= 1

	if m == 0:
		#for i in range(n):
			#nums1[i] = nums2[i]
		nums1[0:n] = nums2[0:n]
	#print m,n,i
	return

nums1 = [1,0]
nums2 = [2]

merge(nums1,1,nums2,1)
print nums1