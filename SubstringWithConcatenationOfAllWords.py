#coding:utf-8

#You are given a string, s, and a list of words, words, that are all of the same length. 
#Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

#For example, given:
#s: "barfoothefoobarman"
#words: ["foo", "bar"]

#You should return the indices: [0,9].
#(order does not matter).


def findSubstring(s,words):

	lens = [len(words[i]) for i in range(len(words))]
	res = []
	delelen = 0

	while s != "":
		ind = [0]*len(words)
		indjudge = [0]*len(words)
		for i in range(len(words)):
			ind[i] = s.find(words[i])
			#ind[i]+lens[i]应该是另一个words的开始坐标
			indjudge[i] = ind[i] + lens[i]
		if -1 in ind: break
		ind.sort()
		indjudge.sort()
		a = ind.pop(0)
		b = indjudge.pop(-1)
		if ind == indjudge: res.append(a+delelen)
		s = s[b:]
		delelen += b

	return res

def findSubstring2(s, words):
    if len(words) == 0:
        return []
    # initialize d, l, ans
    l = len(words[0])
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    i = 0
    ans = []

    # sliding window(s)
    for k in range(l):
        left = k
        subd = {}
        count = 0
        for j in xrange(k, len(s)-l+1, l):
            tword = s[j:j+l]
            # valid word
            if tword in d:
                if tword in subd:
                    subd[tword] += 1
                else:
                    subd[tword] = 1
                count += 1
                while subd[tword] > d[tword]:
                    subd[s[left:left+l]] -= 1
                    left += l
                    count -= 1
                if count == len(words):
                    ans.append(left)
            # not valid
            else:
                left = j + l
                subd = {}
                count = 0

    return ans

def findSubstring3(S,L):
	if not L or not L[0]: return None

	wl = len(L[0])
	total = len(L)*wl

	count_tmpl = collections.defaultdict(int)
	for word in L: count_tmpl[word] += 1
	rtn = []

	for i in range(wl):
		count = copy.copy(count_tmpl)
		j = i
		while j < len(s)-wl+1:
			count[S[j:j+wl]] -= 1
			while count[S[j:j+wl]] < 0:
				count[S[j:j+wl]] += 1
				i += wl
			if j-i == total: rtn.append(i)

	return rtn

def findSubString4(s,words):

	wordmap = {}
	res = []

	wordlen = len(words[0])
	totallen = wordlen * len(words)
	#统计words中各个word数量
	for i in range(len(words)):
		if words[i] in wordmap:
			wordmap[words[i]] += 1
		else:
			wordmap[words[i]] = 1

	#for i in range(len(s)):
	i = 0
	while i+wordlen < len(s):
		tmpstr = s[i:i+wordlen]
		if tmpstr in words and i+totallen <= len(s):
			tmptotal = s[i:i+totallen]
			checkmap = {}
			for j in range(0,totallen,wordlen):
				check = tmptotal[j:j+wordlen]
				if check not in wordmap:
					i += j
					break
				if check in checkmap:
					checkmap[check] += 1
				else:
					checkmap[check] = 1

			if len(checkmap) != len(wordmap):
				i += j
				continue
			flag = True
			for m in wordmap.keys():
				if wordmap[m] != checkmap[m]:
					flag = False

			if flag:
				res.append(i)
				i += totallen
			else:
				i += 1
		else:
			i += 1
	

	print res



s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

print findSubstring2(s,words)