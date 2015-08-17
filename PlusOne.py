#coding:utf-8

#Given a non-negative number represented as an array of digits, plus one to the number.

#The digits are stored such that the most significant digit is at the head of the list.

#题目：[1,2,3,4]+1--->[1,2,3,5]
#由于题目只要加1，因此进位只对末尾连续的9有影响，如[1,4,9,9]+1-->[1,5,0,0]
#因此只需从末尾开始搜索9，遇到9将其变为0，继续往前搜索，直到遇到第一个不是9的数
#在第一个不是9的数上加1，基本完成
#特殊情况：原数字每一位都是9，则要在最前面再加一位1，如[9,9,9]+1-->[1,0,0,0]
def plusOne(digits):
	i = len(digits)-1
	contnine = 0
	while i >= 0:
		if digits[i] != 9:
			break
		else:
			contnine += 1
		i -= 1

	for i in range(contnine):
		digits[-1-i] = 0
	if contnine == len(digits):
		digits.insert(0,1)
	else:
		digits[-1-contnine] += 1
	
	return digits

def plusOne2(digits):
	i = len(digits)-1
	
	while i >= 0:
		if digits[i] != 9:
			break
		else:
			digits[i] = 0
		i -= 1

	if i == -1:
		digits.insert(0,1)
	#elif i == 0:
	#	digits[0] +=1
	else:
		digits[i] += 1
	
	return digits

x = [1,8,9,3]
print plusOne2(x)