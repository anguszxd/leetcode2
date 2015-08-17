#coding:utf-8

#You are climbing a stair case. It takes n steps to reach to the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#本题原型是斐波那契数列
#如n=5，从第5级阶梯反向推导，最后一步可能是1级或2级，
#如果是1级，则前面还有4级，如果是2级，则前面还有3级
#因此，上5级台阶的所有方法是上4级台阶方法数量加上3级台阶方法数量
def climbingStairs(n):
	if n == 1:
		return 1
	if n == 2:
		return 2

	x1, x2, tmp = 1, 2, 0
	for i in range(n-2):
		tmp = x1 + x2
		x1 = x2
		x2 = tmp

	return tmp


n = 4
print climbingStairs(n)