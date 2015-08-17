def LongestPalindromicSubstring(s):
	length = 0
	for i in range(0,len(s)-1):
		if s[i] == s[i+1]:
			temp = 2
			for j in range(1,i+1):
				if i+j+1 <= len(s)-1 and s[i-j] == s[i+j+1]:
					temp += 2
				else:
					break
			if temp > length:
				length = temp
		else:
			temp = 1
			for j in range(1,i+1):
				if i+j <= len(s)-1 and s[i-j] == s[i+j]:
					temp += 2
				else:
					break
			if temp > length:
				length = temp

	return length

def LongestPalindromicSubstring2(s):
	if len(s) == 1:
		return 1,s
	length = 0
	ss = ''
	for i in range(0,len(s)-1):
		temp = 0
		for j in range(0,i+1):
			if i+j+1 <= len(s)-1 and s[i-j] == s[i+j+1]:
				temp += 2
			else:
				break

		if temp > length:
			length = temp
			if j == i:
				ss = s[i-j : i+j+2]
			else:
				ss = s[i-j+1:i+j+1]


		temp = -1
		for k in range(0,i+1):
			if i+k <= len(s)-1 and s[i-k] == s[i+k]:
				temp += 2
			else:
				break
		if temp > length:
			length = temp
			if k == i:
				ss = s[i-k:i+k+1]
			else:
				ss = s[i-k+1:i+k]

	return length,ss


def LongestPalindromicSubstring3(s):
	if len(s) == 1:
		return 1,s
	length = 0
	ss = ''
	for i in range(0,len(s)-1):
		temp1 = 0
		temp2 = -1
		c1=True
		c2=True
		for j in range(0,i+1):
			if i+j+1 <= len(s)-1 and s[i-j] == s[i+j+1] and c1:
				temp1 += 2
			else:
				c1=False
			if i+j <= len(s)-1 and s[i-j] == s[i+j] and c2:
				temp2 += 2
			else:
				c2=False

			if c1==False and c2==False:
				break

		if temp1 > length:
			length = temp1
			if j == i:
				ss = s[i-j : i+j+2]
			else:
				ss = s[i-j+1:i+j+1]

		if temp2 > length:
			length = temp2
			if j == i:
				ss = s[i-j:i+j+1]
			else:
				ss = s[i-j+1:i+j]

	return length,ss


def longestPalindromeDP(s):
	n = len(s)
	longestBegin = 0
	maxLen = 1
	#create a two-dimensional array
	table = [([0]*n) for i in range(n)]

	for i in range(0,n):
		table[i][i] = 1

	for i in range(0,n-1):
		if s[i] == s[i+1]:
			table[i][i+1] = 1
			longestBegin = i
			maxLen =2

	for leng in range(3,n+1):
		for i in range(n-leng+1):
			j = i+leng-1
			if s[i] == s[j] and table[i+1][j-1] == 1:
				table[i][j] = 1
				longestBegin = i
				maxLen = leng
	ss=s[longestBegin:longestBegin+maxLen]

	return longestBegin,maxLen,ss

s = "gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"
#s = raw_input('plz input str:')
#l,ss = LongestPalindromicSubstring3(s)
#print l
#print ss
#print len(ss)
lB,maxL,ss = longestPalindromeDP(s)
print lB
print maxL
print ss
print len(ss)