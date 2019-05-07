# othello_board.py
# Daniel Burns

class OthelloBoard():

	def __init__(self, rowsize=8, columnsize=8):
		self.rowsize = rowsize
		self.columnsize = columnsize
		self.board = [['.' for _ in range(columnsize)] for _ in range(rowsize)]
	
	def printBoard(self):
		print(' ', end='')
		for i in range(len(self.board)):
			print('{:>2}'.format(i), end='')
		print('')
		for i in range(len(self.board)):
			print(i, end='')
			for j in range(len(self.board)):
				print('{:>2}'.format(self.board[i][j]), end='')
			print('')






if __name__ == '__main__':
	othelloBoard = OthelloBoard()
	othelloBoard.printBoard()
