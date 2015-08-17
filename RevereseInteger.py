#coding:utf-8
#思路：用取余的方式取出原数的每一位上的数
#再将其反向*10+下一位
#注意符号
def reverse1(x):
	if x==0:
		return x
	neg = False
	if x< 0:
		neg = True
		x = -x

	ElemList = []
	while x > 0:
		ele = x % 10
		ElemList.append(ele)
		x = x/10

	print ElemList
	res = ElemList[0]
	for i in range (1,len(ElemList)):
		res = res*10+ElemList[i]

	if neg:
		res = -res
#注意溢出的问题
	if abs(result)>2147483648:
		return 0
	else:
		return res

#思路相同，过程更加简洁精炼
def reverse(self, x):
    if x >= 0:
		leave = x
		sign = 1
	else:
		leave = -x
		sign = -1

	result = 0
	while 0 != leave:
		result = result * 10 + leave % 10
		leave /= 10
            
	if abs(result)>2147483648:
		return 0
	else:
		return result * sign

x=-15231
r=reverse(x)
print r