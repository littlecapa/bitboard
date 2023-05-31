import sys
sys.path.append('..')

from src.bit_board import BitBoard

import chess

board = chess.Board()
bb = BitBoard(board)

print (bb.get_pretty_string())