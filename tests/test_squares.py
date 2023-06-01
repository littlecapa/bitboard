import chess

board = chess.Board()
board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")
board.push_san("Nc6")
board.push_san("Bc4")
board.push_san("Nf6")

print(board)

new_board = board.mirror()
print(new_board)

new_board = board.transform(chess.flip_vertical)
print(new_board)
new_board = board.transform(chess.flip_horizontal)
print(new_board)
