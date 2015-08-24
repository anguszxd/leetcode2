#coding:utf-8

#DP练习题：平面上有M*N的格子，每个格子上放有若干个苹果，从左上角出发，
#每次只能向下或向右移动，每到一个格子上就把其中的苹果收集起来，问最多能收集多少个苹果？

#Solution:用S[i][j]表示达到ij位置时能获得的最多的苹果数量(状态)，则状态转移方程为：
#S[i][j] = A[i][j]+max(S[i][j-1],if j > 0;S[i-1][j],if i > 0)，即为得到当前状态的值，
#我们需要得到前一状态S[i][j-1]和S[i-1][j]的状态值

apples = [[1,4,2,7],[5,6,10,3],[8,4,9,2]]
M, N = len(apples), len(apples[0])

S = [[0 for i in range(N)] for j in range(M)]

S[0][0] = apples[0][0]
for i in range(1,N,1):
	S[0][i] = apples[0][i]+S[0][i-1]
for j in range(1,M,1):
	S[j][0] = apples[j][0]+S[j-1][0]

for i in range(1,M,1):
	for j in range(1,N,1):
		S[i][j] = apples[i][j]+max(S[i-1][j],S[i][j-1])
print S[M-1][N-1]