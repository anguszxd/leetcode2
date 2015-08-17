#coding:utf-8

#Write a program to solve a Sudoku puzzle by filling the empty cells.

#Empty cells are indicated by the character '.'.

#You may assume that there will be only one unique solution.

#用回溯法尝试每一种可能性，直到求出最后的解
#import ValidSudoku
import string

#找到当前待填空格可能的值
def LatentElem(row,column,blank):
	#elem = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'.':0}
	latElem = ['1','2','3','4','5','6','7','8','9','.']
	for i in range(9):
		if row[i] in latElem:
			latElem.pop(latElem.index(row[i]))
	for i in range(9):
		if column[i] in latElem:
			latElem.pop(latElem.index(column[i]))
	for i in range(3):
		for j in range(3):
			if blank[i][j] in latElem:
				latElem.pop(latElem.index(blank[i][j]))

	if '.' in latElem:
		latElem.pop(latElem.index('.'))

	return latElem

#使用递归的方式进行回溯，测试当前待填空格的值
#回溯的条件：1、当前待填空格没有潜在值，退回到上一步
#2、当前待填空格原有的潜在值都以测试，还没得到结果，继续回溯
#递归结束条件：所有空格都填满
def BlankOperate(board,cflag):
	if not cflag:
		return cflag
	for i in range(9):
		flag = False
		for j in range(9):
			if board[i][j] == '.':
				flag = True
				break

		if flag: break

	#print i,j
	row = board[i]
	column = [board[m][j] for m in range(9)]
	blank = [[board[m][n] for n in range((j/3)*3,(j/3)*3+3)] for m in range((i/3)*3,(i/3)*3+3)]
	latelem = LatentElem(row,column,blank)
	#print latelem
	if len(latelem) == 0:
		return True

	contflag = False
	for l in range(len(latelem)):
		board[i][j] = latelem[l]
		for m in range(9):
			for n in range(9):
				if board[m][n] == '.':
					contflag = True
		contflag = BlankOperate(board,contflag)
		if not contflag:
			break

	


	if l == len(latelem) - 1 and contflag:
		board[i][j] = '.'
		return True

	#else:
	#	return contflag



def solveSudoku(board):
	for i in range(9):
		board[i] = list(board[i])
	return board



#ValSudoku = [['5','3','.','.','7','.','.','.','.'],
#			 ['6','.','.','1','9','5','.','.','.'],
#			 ['.','9','8','.','.','.','.','6','.'],
#			 ['8','.','.','.','6','.','.','.','3'],
#			 ['4','.','.','8','.','3','.','.','1'],
#			 ['7','.','.','.','2','.','.','.','6'],
#			 ['.','6','.','.','.','.','2','8','.'],
#			 ['.','.','.','4','1','9','.','.','5'],
#			 ['.','.','.','.','8','.','.','7','9']]

Sudo = [".687...19","....4...3","..2......",".8529713.","9.638.257",".3.15.948","..4561.7.",".5..2.684",".23478.91"]

sudo = solveSudoku(Sudo)
c = BlankOperate(sudo,True)
print sudo

