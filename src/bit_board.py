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

    def is_any_castling_possible(self):
        return self.board.has_castling_rights(chess.WHITE) or self.board.has_castling_rights(chess.BLACK)

    def are_any_pawns_remaining(self):
        return any(self.board.pieces(chess.PAWN, chess.WHITE)) or any(self.board.pieces(chess.PAWN, chess.BLACK))
    
    def flip_files(self):
        # a -> h
        # ...
        # h -> a
        if not(self.is_any_castling_possible()):
            self.create_bit_board(self.board.transform(chess.flip_horizontal))
        else:
            raise("Casting possible")

    def flip_ranks(self):
        # 1 -> 8
        # ...
        # 8 -> 1
        if not(self.are_any_pawns_remaining()):
            self.create_bit_board(self.boardchess.transform(chess.flip_vertical))
        else:
            raise("Still Pawns on the board")                     

    def board2bit_board(self, board):
        bit_board = []
        for color, _ in COLORS.items():
            for piece, _ in PIECES.items():
                bit_board.append(self.board.pieces(piece, color))
        return bit_board
    
    def get_bit_board(self):
        return self.bit_board
    
    def bit_board2str(self, bit_board):
        i = 0
        pstr = ""
        for color, color_name in COLORS.items():
            for piece, piece_name in PIECES.items():
                pstr += color_name + " " + piece_name + "\n"
                pstr += str(bit_board[i])
                pstr += "\n"
                i += 1
        return pstr
    
    def get_pretty_string(self):
        return self.bit_board2str(self.bit_board)
    
    def change_colors(self):
        new_board = self.board.mirror()
        new_board.turn = not self.board.turn
        new_board.set_castling_fen(self.board.castling_xfen())
        # Mirror the en passant square
        if self.board.ep_square is not None:
            file, rank = chess.square_file(self.board.ep_square), chess.square_rank(self.board.ep_square)
            mirrored_file = chess.FILE_NAMES.index(file)
            mirrored_ep_square = chess.square(chess.FILE_NAMES[mirrored_file], rank)
            new_board.ep_square = mirrored_ep_square
        else:
            new_board.ep_square = None
        
        # Determine the valid castling rights for the new board
        valid_castling_rights = ""
        if self.board.has_kingside_castling_rights(chess.BLACK):
            valid_castling_rights += 'K'
        if self.board.has_queenside_castling_rights(chess.BLACK):
            valid_castling_rights += 'Q'
        if self.board.has_kingside_castling_rights(chess.WHITE):
            valid_castling_rights += 'k'
        if self.board.has_queenside_castling_rights(chess.WHITE):
            valid_castling_rights += 'q'
        
        # Set the valid castling rights on the new board
        new_board.set_castling_fen(valid_castling_rights)
        self.create_bit_board(new_board)



        






