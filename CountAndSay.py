#coding:utf-8

#The count-and-say sequence is the sequence of integers beginning as follows:
#1, 11, 21, 1211, 111221, ...

#1 is read off as "one 1" or 11.
#11 is read off as "two 1s" or 21.
#21 is read off as "one 2, then one 1" or 1211.
#Given an integer n, generate the nth sequence.

def countsay(x):
	s = list(str(x))
	print s
	print s[0]
	for i in range(x):
		tmp = []
		tmpnum = 1
		tmpind = 0
		if len(s) == 1:
			#tmp[0] = str(1)
			#tmp.append(s[0])
			tmp.insert(0,'1')
			tmp.append(s[0])
			s = tmp
			continue
		m = len(s)-1
		for j in range(m):
			if s[j] == s[j+1]:
				tmpnum += 1
			else:
				#tmp[tmpind] = str(tmpnum)
				tmp.append(str(tmpnum))
				tmp.append(s[j+1])
				tmpnum = 1
		s = tmp.append(s[-1])
		print tmp
	return s

x = 3
print countsay(x)