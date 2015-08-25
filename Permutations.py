#coding:utf-8

#Given a collection of numbers, return all possible permutations.

#For example,
#[1,2,3] have the following permutations:
#[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

def permute(nums,ans,path):
	if len(nums) == 1:
		ans.append(path+nums)
		return

	for i in range(len(nums)):
		permute(nums[0:i]+nums[i+1:],ans,path+[nums[i]])


A = [1,2,3,4]
ans = []
path = []
permute(A,ans,path)

print ans