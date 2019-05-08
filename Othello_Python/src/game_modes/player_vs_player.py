# player_vs_player
# Daniel Burns

import os

from src.board_setup.othello_board import OthelloBoard

class PlayerVsPlayer():

	def __init__(self):
		self.row = None
		self.column = None
		self.turn = 1
		self.gameBoard = OthelloBoard()
	
	def mainExecution(self):
		os.system('clear')
		self.gameBoard.printBoard()
		print('\nPlayer X goes first', end='')
		while not self.gameBoard.isGameFinished():
			if self.turn % 2: print('\nPlayer X:')
			else: print('\nPlayer O:')
			print('---------', end='\n\n')
			self.column = int(input('Enter X Coordinate: '))
			self.row = int(input('Enter Y Coordinate: '))
			if self.gameBoard.board[self.row][self.column] != '.':
				print('\nThere is already a piece there.. Please re-enter X and Y coordinates', end='\n\n')
				continue
			if not self.isConnectedToOtherPiece():
				print('\nPiece must be connected to another piece.. Please re-enter X and Y coordinates', end='\n\n')
				continue
			if self.turn % 2:
				self.gameBoard.board[self.row][self.column] = 'X'
			else:
				self.gameBoard.board[self.row][self.column] = 'O'
			self.iterateBoard()
			self.turn += 1
			os.system('clear')
			self.gameBoard.printBoard()

		xCount = 0
		oCount = 0
		for i in range(len(self.gameBoard.rowsize)):
			for j in range(len(self.gameBoard.columnsize)):
				if self.gameBoard.board[i][j] == 'X': xCount += 1
				elif self.gameBoard.board[i][j] == 'O': oCount += 1
		if xCount > oCount: print('Player X wins!')
		elif xCount < oCount: print('Player O wins!')
		else: print("It's a tie!")
		print('Thank you for playing', end='\n\n')
	
	def isConnectedToOtherPiece(self):
		for i in range(-1, 2):
			for j in range(-1, 2):
				if self.row + i < self.gameBoard.rowsize and self.row + i >= 0 and \
					self.column + j < self.gameBoard.columnsize and \
					self.column + j >= 0:
					if self.gameBoard.board[self.row + i][self.column + j] \
						!= '.':
						return True
		return False
	
	def iterateBoard(self):
		if self.gameBoard.captureLeft(self.row, self.column):
			if self.turn % 2: self.gameBoard.board[self.row][self.column - 1] = 'X'
			else: self.gameBoard.board[self.row][self.column - 1] = 'O'
		if self.gameBoard.captureRight(self.row, self.column):
			if self.turn % 2: self.gameBoard.board[self.row][self.column + 1] = 'X'
			else: self.gameBoard.board[self.row][self.column + 1] = 'O'
		if self.gameBoard.captureUp(self.row, self.column):
			if self.turn % 2: self.gameBoard.board[self.row - 1][self.column] = 'X'
			else: self.gameBoard.board[self.row - 1][self.column] = 'O'
		if self.gameBoard.captureDown(self.row, self.column):
			if self.turn % 2: self.gameBoard.board[self.row + 1][self.column] = 'X'
			else: self.gameBoard.board[self.row + 1][self.column] = 'O'
		if self.gameBoard.captureUpLeft(self.row, self.column):
			if self.turn % 2: self.gameBoard.board[self.row - 1][self.column - 1] = 'X'
			else: self.gameBoard.board[self.row - 1][self.column - 1] = 'O'
		if self.gameBoard.captureUpRight(self.row, self.column):
			if self.turn % 2: self.gameBoard.board[self.row - 1][self.column + 1] = 'X'
			else: self.gameBoard.board[self.row - 1][self.column + 1] = 'O'
		if self.gameBoard.captureDownLeft(self.row, self.column):
			if self.turn % 2: self.gameBoard.board[self.row + 1][self.column - 1] = 'X'
			else: self.gameBoard.board[self.row + 1][self.column - 1] = 'O'
		if self.gameBoard.captureDownRight(self.row, self.column):
			if self.turn % 2: self.gameBoard.board[self.row + 1][self.column + 1] = 'X'
			else: self.gameBoard.board[self.row + 1][self.column + 1] = 'O'
