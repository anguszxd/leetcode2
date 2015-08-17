def lengthOfLongestSubstring(s):
	#create a dict,hash table
	process={}
	#l = list(s)
	idx = -1 #idx:start id of current substring
	length = 0
	for i in range(len(s)):
		print process
		print idx
		#if s[i] in process:
		if s[i] in process and process[s[i]] > idx:
			idx = process[s[i]]

		if i - idx >length:
			length = i - idx
		process[s[i]] = i
	#print process
	return length

s='abcadefg'
length=lengthOfLongestSubstring(s)
#lengthOfLongestSubstring(s)
print length
