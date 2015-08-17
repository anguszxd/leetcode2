#coding:utf-8
#Determine if a Sudoku is valid
#The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

#A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

#方法一：按照数独规则分别检查行、列、块是否有效
def isValidSudoku(board):
	#按行查是否有效
	for i in range(9):
		elem = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'.':0}
		for j in range(9):
			if elem[board[i][j]] == 0 or board[i][j] == '.':
				elem[board[i][j]] += 1
			else:
				print "row error"
				print i,j,board[i][j],elem[board[i][j]]
				return False
	#案列检查是否有效
	for i in range(9):
		elem = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'.':0}
		for j in range(9):
			if elem[board[j][i]] == 0 or board[j][i] == '.':
				elem[board[j][i]] += 1
			else:
				print "column error"
				print i,j,board[j][i],elem[board[j][i]]
				return False
	#按块检查是否有效
	for i in [0,3,6]:
		for j in [0,3,6]:
			elem = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'.':0}
			for m in range(3):
				for n in range(3):
					if elem[board[i+m][j+n]] == 0 or board[i+m][j+n] == '.':
						elem[board[i+m][j+n]] += 1
					else:
						print "block error"
						print i+m,j+n,board[i+m][j+n]
						return False

	return True

#效率更高的方法，只需要遍历一次，
#将当前位置的元素分别放入其所在的rows/columns/blocks中
#下一个元素进来时，先检查其所在rows/columns/blocks中是否已经有了该元素
#如果有，则该数独是错误的，返回False，否则继续遍历知道所有元素遍历结束
#blocks是3x3的矩阵
def isValid(board):

	rows = [[],[],[],[],[],[],[],[],[]]
	columns = [[],[],[],[],[],[],[],[],[]]
	blocks = [[[],[],[]],[[],[],[]],[[],[],[]]]

	for i in range(9):
		for j in range(9):
			if board[i][j] == '.':
				continue
			if (board[i][j] not in rows[i]) and (board[i][j] not in columns[j]) and (board[i][j] not in blocks[i/3][j/3]):
				rows[i].append(board[i][j])
				columns[j].append(board[i][j])
				blocks[i/3][j/3].append(board[i][j])
			else:
				print i,j,board[j][i]
				return False

	return True


ValSudoku = [['5','3','.','.','7','.','.','.','.'],
			 ['6','.','.','1','9','5','.','.','.'],
			 ['.','9','8','.','.','.','.','6','.'],
			 ['8','.','.','.','6','.','.','.','3'],
			 ['4','.','.','8','.','3','.','.','1'],
			 ['7','.','.','.','2','.','.','.','6'],
			 ['.','6','.','.','.','.','2','8','.'],
			 ['.','.','.','4','1','9','.','.','5'],
			 ['.','.','.','.','8','.','.','7','9']]

print ValSudoku

print isValid(ValSudoku)