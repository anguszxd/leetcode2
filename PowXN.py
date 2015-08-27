#coding:utf-8

#Implement pow(x, n).

def myPow(x, n):
	if n < 0:
		x = 1/x
		n = -n
	cur  = x
	ans = 1
	while n > 0:
		if n & 0x1:
			ans *= cur
		cur = cur*cur
		n = n >> 1

	return ans
x = 34.00515
n = -3
print myPow(x, n)
print pow(x, n)