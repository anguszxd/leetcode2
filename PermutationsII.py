#coding:utf-8

#Given a collection of numbers that might contain duplicates, return all possible unique permutations.


#For example,
#[1,1,2] have the following unique permutations:
#[1,1,2], [1,2,1], and [2,1,1].

#Solution:跟前面的全排列类似，改进的地方在于先判断放在第一位的元素有没有出现过，
#如果已经使用过了，就跳过该循环
def permute(nums,ans,path):
	if len(nums) == 1:
		#if path+nums not in ans:
		ans.append(path+nums)
		return
	used = []
	for i in range(len(nums)):
		if nums[i] not in used:
			used.append(nums[i])
			permute(nums[0:i]+nums[i+1:],ans,path+[nums[i]])
			#used.append(nums[i])


A = [1,1,0,0,1,-1,-1,1]
ans = []
path = []
permute(A,ans,path)

print ans,len(ans)