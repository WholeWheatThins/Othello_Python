# main
# Daniel Burns

from src.board_setup.othello_board import OthelloBoard
from src.game_modes.player_vs_player import PlayerVsPlayer

def main():
	playerVsPlayer = PlayerVsPlayer()
	playerVsPlayer.mainExecution()

if __name__ == '__main__':
	main()
