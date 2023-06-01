import sys
sys.path.append('..')

from src.bit_board import BitBoard

# Specify the path to the local library/module
library_path = "/Users/littlecapa/GIT/python/ChessEvaluator/src"

# Add the library path to the system path
sys.path.append(library_path)

from chess_eval import ChessEvaluator


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

evaluator = ChessEvaluator()

bb = BitBoard(board)

input = bb.get_input_tensor()
print(input)

eval = evaluator.eval_position(input)
print(f"Eval: {eval}")