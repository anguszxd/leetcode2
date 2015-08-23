#coding:utf-8

#不是leetcode中的问题，练习动态规划法用的
#现有面值为1,3,5的硬币数量若干，问组成11元最少需要多少个硬币？

#def leastCoins(coins, money):


coins = [1, 3, 5]
money = 20
Min = []
Min.append(0)

for i in range(1,money+1,1):
	Min.append(money+1)	
	for j in range(len(coins)):
		if coins[j] <= i and Min[i-coins[j]] + 1 < Min[i]:
			Min[i] = Min[i-coins[j]] + 1

print Min[money]