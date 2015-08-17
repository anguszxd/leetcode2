def addTwoNumbers(l1,l2):
	res = []
	t1 = 0
	for i in range(len(l1)):
		t2 = t1
		temp = l1[i] + l2[i]
		if temp >= 10:
			temp = temp -10
			t1 = 1
		else:
			t1 = 0
		#res[i] = temp + t2
		res = res + [temp + t2]
	if t1 == 1:
		res = res + [1]

	return res

l1 = [5,4,3,5]
l2 = [5,6,4,6]

result = addTwoNumbers(l1,l2)
print result

