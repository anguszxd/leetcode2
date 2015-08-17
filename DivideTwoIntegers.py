#coding:utf-8
#Divide two integers without using multiplication, division and mod operator.

#If it is overflow, return MAX_INT.

#题目要求不能用乘除取余等，所以只能用加减法和位运算完成除法操作
#先想到用加减法做，但这样速度比较慢，在leetcode中超时
def divideTwoInts(dividend, divisor):
	intMax, intMin = 2147483647, -2147483648
	sign = 1
	if 0 in [dividend, divisor]:
		return 0
	elif dividend < 0 < divisor or divisor < 0 < dividend:
		sign = -1
		dividend, divisor = abs(dividend), abs(divisor)
	else:
		dividend, divisor = abs(dividend), abs(divisor)
	res = 0
	while dividend >= divisor:
		tmp, val = divisor, 1
		while dividend >= tmp:
			res += val
			dividend -= tmp
			tmp += tmp
			val += val
	if sign == 1:
		return min(intMax, res)
	else:
		return max(intMin, 0-res)


#使用位运算的方法
#左移1位<<:相当于原数值乘以2，如4<<1=8
#右移1位>>:相当于原数值除以2，如4>>1=2
#利用左移相当于乘2的性质，扩大除数，如(15,3)，加快被除数减小的速度
#15-3=12>0,12-6=6>0,这两次减法包含了1+2个除数3
#再扩大除数，6-6*2=-6<0，说明此时除数太大，要返回到最初的除数等于3
#6-3=3>0,再加1个除数3，在扩大除数3-6=-3<0，同样除数太大，返回最初的除数
#3-3=0，除尽，总的减去的除数个数为：1+2+1+1=5
#即15/3=5

def divide(dividend,divisor):
	sign = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
	a, b = abs(dividend), abs(divisor)
	ret, c = 0, 0

	while a >= b:
		c = b	
		i = 0
		while a >= c:
			a -= c
			ret += (1<<i)
			i += 1
			c <<= 1
			print "ret=",ret
			print "a=",a
			print "c=",c

	if sign:
		ret = -ret
	return min(max(-2147483648, ret), 2147483647)


dividend = 15
divisor = 3

print divide(dividend,divisor)