import sys
sys.path.append('..')

from src.bit_board import BitBoard

import chess

board = chess.Board()
board = chess.Board()
board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")
board.push_san("Nc6")
board.push_san("Bc4")
board.push_san("Nf6")
board.push_san("Ng5")
board.push_san("b5")
board.push_san("Bf7")
board.push_san("Ke7")

bb = BitBoard(board)
print(bb.get_pretty_string())
if bb.is_any_castling_possible():
    print("Castling possible")
else:
    print("No Castling possible")

print("After flip!")
bb.change_colors()
print(bb.get_pretty_string())
#bb.flip_files()
#print(bb.get_pretty_string())

board.push_san("O-O")
bb = BitBoard(board)

if bb.is_any_castling_possible():
    print("Castling possible")
else:
    print("No Castling possible")
    bb.flip_files()
    print(bb.get_pretty_string())


fen = "rnbqk1nr/8/3b4/4N3/8/8/8/RNBQKB1R w - - 0 7"
board = chess.Board(fen)
bb = BitBoard(board)
print(bb.get_pretty_string())
bb.flip_files()
print(bb.get_pretty_string())

