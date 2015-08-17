#coding:utf-8
#该方法思路：取最前一位和最末尾一位进行比较，看两者是否相同
#若相同则在原数上去除最高位和最低位，继续进行比较
#但该方法存在的问题是：去除最高位和最低位后，余下的不一定能成为数
#如：1000001，去除最高位最低位后全是0，不是一个数了
def isPalindrome(x):
	x1 = x
	digit = 0
	isPalin = True

	while x1 > 0:
		x1 /= 10
		digit += 1
	print digit

	x2 = x
	while x2 > 10:
		tail = x2%10
		head = x2/(pow(10,digit-1))
		if tail == head:
			digit -= 2
			x2 /= 10
			x2 -= head*pow(10,digit)
			print x2
		else:
			isPalin = False
			break

	return isPalin


#方法2：直接使用翻转整数的方法(回文整数的特点是，翻转后与原数值相同)
#将整数翻转后，与原数值进行比较，看是否相同
#这里认为负数是不能是回文整数
def isPalindrome2(x):
	if x < 0:
		return False
	if x == 0:
		return True

	leave = x
	result = 0
	while 0 != leave:
		result = result * 10 + leave % 10
		leave /= 10
            
	print leave
	return x == result

x = 1
print isPalindrome2(x)
