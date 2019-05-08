# othello_board
# Daniel Burns

class OthelloBoard():

	def __init__(self, rowsize=8, columnsize=8):
		self.rowsize = rowsize
		self.columnsize = columnsize
		self.board = [['.' for _ in range(columnsize)] for _ in range(rowsize)]
		self.board[int((len(self.board) / 2) - 1)][int((len(self.board) / 2) - 1)] = 'X'
		self.board[int(len(self.board) / 2)][int(len(self.board) / 2)] = 'X'
		self.board[int((len(self.board) / 2) - 1)][int(len(self.board) / 2)] = 'O'
		self.board[int(len(self.board) / 2)][int((len(self.board) / 2) - 1)] = 'O'
	
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
	
	def isGameFinished(self):
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				if self.board[i][j] == '.': return False
		return True

	def captureLeft(self, row, column):
		if ((column - 2 >= 0) and \
			(self.board[row][column - 1] != '.' and \
			self.board[row][column - 1] != self.board[row][column]) and \
			(self.board[row][column - 2] == self.board[row][column])):
			return True
		return False
	
	def captureRight(self, row, column):
		if ((column + 2 < self.columnsize) and \
			(self.board[row][column + 1] != '.' and \
			self.board[row][column + 1] != self.board[row][column]) and \
			(self.board[row][column + 2] == self.board[row][column])):
			return True
		return False
	
	def captureUp(self, row, column):
		if ((row - 2 >= 0) and \
			(self.board[row - 1][column] != '.' and \
			self.board[row - 1][column] != self.board[row][column]) and \
			(self.board[row - 2][column] == self.board[row][column])):
			return True
		return False
	
	def captureDown(self, row, column):
		if ((row + 2 < self.rowsize) and \
			(self.board[row + 1][column] != '.' and \
			self.board[row + 1][column] != self.board[row][column]) and \
			(self.board[row + 2][column] == self.board[row][column])):
			return True
		return False
	
	def captureUpLeft(self, row, column):
		if ((row - 2 >= 0) and (column - 2 >= 0) and \
			(self.board[row - 1][column - 1] != '.' and \
			self.board[row - 1][column - 1] != self.board[row][column]) and \
			(self.board[row - 2][column - 2] == self.board[row][column])):
			return True
		return False

	def captureUpRight(self, row, column):
		if ((row - 2 >= 0) and (column + 2 < self.columnsize) and \
			(self.board[row - 1][column + 1] != '.' and \
			self.board[row - 1][column + 1] != self.board[row][column]) and \
			(self.board[row - 2][column + 2] == self.board[row][column])):
			return True
		return False
	
	def captureDownLeft(self, row, column):
		if ((row + 2 < self.rowsize) and (column - 2 >= 0) and \
			(self.board[row + 1][column - 1] != '.' and \
			self.board[row + 1][column - 1] != self.board[row][column]) and \
			(self.board[row + 2][column - 2] == self.board[row][column])):
			return True
		return False
	
	def captureDownRight(self, row, column):
		if ((row + 2 < self.rowsize) and (column + 2 < self.columnsize) and \
			(self.board[row + 1][column + 1] != '.' and \
			self.board[row + 1][column + 1] != self.board[row][column]) and \
			(self.board[row + 2][column + 2] == self.board[row][column])):
			return True
		return False
