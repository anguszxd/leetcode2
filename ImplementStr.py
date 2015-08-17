#coding:utf-8
#Returns the index of the first occurrence of 
#needle in haystack, or -1 if needle is not part of haystack.

#任务：寻找第一个字串

def implementStr(haystack,needle):
	idx = -1

	if needle == '':
		return 0
	if haystack == '':
		return idx

	for i in range(len(haystack) - len(needle) +1):
		#if haystack[i] == needle[0] and (i + len(needle)) <= len(haystack):
		if haystack[i] == needle[0]:
			if haystack[i:i+len(needle)] == needle:
				idx = i
				break

	return idx


hay = 'ninoleafabc'
needle = 'abc'
print implementStr(hay,needle)