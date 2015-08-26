#coding:utf-8

#Given an array of strings, group anagrams together.

#For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
#Return:

#[
#  ["ate", "eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
#Note:
#For the return value, each inner list's elements must follow the lexicographic order.
#All inputs will be in lower-case.

def groupAnagrams(strs):
	letters = []
	ans = []
	for i in range(len(strs)):
		tmplist = sort(list(strs[i]))
		if tmplist not in letters:
			letters.append(tmplist)
			ans.append([strs[i]])
		else:
			ind = letters.index(tmplist)
			flag = True
			for j in range(1,len(ans[ind])+1,1):
				if strs[i] < ans[ind][j-1]:
					ans[ind].insert(j-1,strs[i])
					print "insert here"
					flag = False
					break
			if flag:
				ans[ind].append(strs[i])
		print ans

	return ans




def sort(array):
	for i in range(len(array)-1,-1,-1):
		for j in range(i):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]

	return array

strs = ["",""]
l = [6,5,4,3,2,1]
print groupAnagrams(strs)
