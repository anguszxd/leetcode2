#coding:utf-8

#Given two binary strings, return their sum (also a binary string).

#For example,
#a = "11"
#b = "1"
#Return "100".

#二进制加法，不采用进制转化的方式相加
#注意：1.两个数位数不同，先将位数少的数字前补上'0'，使两者位数相同
#2.每位数字相加结果由la[i],lb[i],carry位'1'的个数决定结果当前位及是否进位
#就是在每一位上进行全加器的操作
#3.如果最后carry='1'，说明最高位要进位，要在最前面添加一位
def binaryAdd(a,b):
	#la = list(a)
	#lb = list(b)
	if len(a) > len(b):
		b = '0'*(len(a)-len(b))+b
	else:
		a = '0'*(len(b)-len(a))+a
	
	elem = {0:'00',1:'01',2:'10',3:'11'}
	carry = '0'

	res = ['0']*len(a)
	#实现全加器(full-adder)的过程
	for i in range(len(a)-1,-1,-1):
		unit = [a[i],b[i],carry]
		localres = elem[unit.count('1')]
		res[i] = localres[1]
		carry = localres[0]

	if carry == '1':
		res.insert(0,'1')
	return ''.join(res)

#eval:将表示二进制数的字符串转换为十进制int数字
#bin:将十进制数字转换为表示二进制数字的字符串，字符串最前面是"0b"
def addBinary(a,b):
	return bin(eval('0b' + a) + eval('0b' + b))[2:]

def addBinary2(a,b):
	return bin(int(a, 2)+int(b, 2))[2:]

a = "1"
b = "11111"

print binaryAdd(a,b)