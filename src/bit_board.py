import chess

COLORS = {
    chess.WHITE: 'white',
    chess.BLACK: 'black'
}

PIECES = {
    chess.PAWN: 'Pawn', 
    chess.KNIGHT: 'Knight', 
    chess.BISHOP: 'Bishop', 
    chess.ROOK: 'Rook', 
    chess.KING: 'King', 
    chess.QUEEN: 'Queen'}

class BitBoard:

    def __init__(self, board):
        self.create_bit_board(board)

    def set_board(self, board):
        self.create_bit_board(board)

    def create_bit_board(self, board):
        self.board = board
        self.bit_board = self.board2bit_board(board)
        
    def board2bit_board(self, board):
        bit_board = []
        for color, _ in COLORS.items():
            for piece, _ in PIECES.items():
                bit_board.append(self.board.pieces(piece, color))
        return bit_board
    
    def get_bit_board(self):
        return self.bit_board
    
    def get_pretty_string(self):
        i = 0
        pstr = ""
        for color, color_name in COLORS.items():
            for piece, piece_name in PIECES.items():
                pstr += color_name + " " + piece_name + "\n"
                #for j in range(8):
                #    pstr += str((self.bit_board[i] >> (7-j)) & 1)
                pstr += str(self.bit_board[i])
                i += 1
                pstr += "\n"
        return pstr
    
    def print_bitmap(bitmap, width):
        for i in range(len(bitmap)):
            for j in range(8):
                # Extract each bit from the byte
                bit = (bitmap[i] >> (7 - j)) & 1
                print(bit, end="")
            if (i + 1) % width == 0:
                print()
            else:
                print(" ", end="")
                
        
