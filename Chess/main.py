class Chessboard:
    def __init__(self):
        self.board = [['' for _ in range(8)] for _ in range(8)]

    @staticmethod
    def startgame() -> None:
        white_rookA = Rook('White', (0, 0))
        chessboard.place_piece(white_rookA, 0, 0)

        white_knightA = Knight('White', (0, 1))
        chessboard.place_piece(white_knightA, 0, 1)

        white_bishopB = Bishop('White', (0, 2))
        chessboard.place_piece(white_bishopB, 0, 2)

        white_queen = Queen('White', (0, 3))
        chessboard.place_piece(white_queen, 0, 3)

        white_king = King('White', (0, 4))
        chessboard.place_piece(white_king, 0, 4)

        white_bishopW = Bishop('White', (0, 5))
        chessboard.place_piece(white_bishopW, 0, 5)

        white_knightB = Knight('White', (0, 6))
        chessboard.place_piece(white_knightB, 0, 6)

        white_rookB = Rook('White', (0, 7))
        chessboard.place_piece(white_rookB, 0, 7)

        white_pawnA = Pawn('White', (1, 0))
        chessboard.place_piece(white_pawnA, 1, 0)

        white_pawnB = Pawn('White', (1, 1))
        chessboard.place_piece(white_pawnB, 1, 1)

        white_pawnC = Pawn('White', (1, 2))
        chessboard.place_piece(white_pawnC, 1, 2)

        white_pawnD = Pawn('White', (1, 3))
        chessboard.place_piece(white_pawnD, 1, 3)

        white_pawnE = Pawn('White', (1, 4))
        chessboard.place_piece(white_pawnE, 1, 4)

        white_pawnF = Pawn('White', (1, 5))
        chessboard.place_piece(white_pawnF, 1, 5)

        white_pawnG = Pawn('White', (1, 6))
        chessboard.place_piece(white_pawnG, 1, 6)

        white_pawnH = Pawn('White', (1, 7))
        chessboard.place_piece(white_pawnH, 1, 7)

        black_rookA = Rook('Black', (7, 0))
        chessboard.place_piece(black_rookA, 7, 0)

        black_knightA = Knight('Black', (7, 1))
        chessboard.place_piece(black_knightA, 7, 1)

        black_bishopW = Bishop('Black', (7, 2))
        chessboard.place_piece(black_bishopW, 7, 2)

        black_queen = Queen('Black', (7, 3))
        chessboard.place_piece(black_queen, 7, 3)

        black_king = King('Black', (7, 4))
        chessboard.place_piece(black_king, 7, 4)

        black_bishopB = Bishop('Black', (7, 5))
        chessboard.place_piece(black_bishopB, 7, 5)

        black_knightB = Knight('Black', (7, 6))
        chessboard.place_piece(black_knightB, 7, 6)

        black_rookB = Rook('Black', (7, 7))
        chessboard.place_piece(black_rookB, 7, 7)

        black_pawnA = Pawn('Black', (6, 0))
        chessboard.place_piece(black_pawnA, 6, 0)

        black_pawnB = Pawn('Black', (6, 1))
        chessboard.place_piece(black_pawnB, 6, 1)

        black_pawnC = Pawn('Black', (6, 2))
        chessboard.place_piece(black_pawnC, 6, 2)

        black_pawnD = Pawn('Black', (6, 3))
        chessboard.place_piece(black_pawnD, 6, 3)

        black_pawnE = Pawn('Black', (6, 4))
        chessboard.place_piece(black_pawnE, 6, 4)

        black_pawnF = Pawn('Black', (6, 5))
        chessboard.place_piece(black_pawnF, 6, 5)

        black_pawnG = Pawn('Black', (6, 6))
        chessboard.place_piece(black_pawnG, 6, 6)

        black_pawnH = Pawn('Black', (6, 7))
        chessboard.place_piece(black_pawnH, 6, 7)

    def print_board(self):
        for row in self.board:
            print(row)

    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def move_piece(self, turn, en_passant, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        result, en_passant = self.is_valid_move(piece, turn, en_passant, start_row, start_col, end_row, end_col)
        if not piece:
            print("No piece found at the specified position.")
            return turn, en_passant
        if result:  # self.is_valid_move(piece, turn, en_passant, start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = ''
            piece.position = (end_row, end_col)
            turn = not turn
            return turn, en_passant
        else:
            print("Invalid move.")
            return turn, en_passant

    def is_valid_move(self, piece, turn, en_passant, start_row, start_col, end_row, end_col):
        target_piece = self.board[end_row][end_col]
        try:
            if target_piece and target_piece.color == piece.color:                                                      #Ruch na zajęte pole przez figurę tego samego koloru
                return False, None
        except:
            return False, None

        if (turn == True and piece.color == "Black") or (turn == False and piece.color == "White"):                 #Ruch czarnym, jak jest ruch białych i na odwrót
            return False, None
        if isinstance(piece, Pawn):
            # Logika dla pionka białego
            if piece.color == 'White':
                if start_row == 1:
                    if end_row - start_row in (1, 2) and start_col == end_col and not self.board[end_row][end_col]: #Jeżeli to pierwszy ruch białego i ruszył się o jedno lub dwa pola do przodu
                        if (end_row - start_row) == 2:                                                              #dodatkowo jeżeli ruszył się o 2, to może zostać zbity w przelocie
                            en_passant = [end_row-1, end_col]
                        return True, en_passant
                    elif (                                                                                          #Czy jest czarna figura możliwa do zbicia po skosie o jedno pole
                            end_row - start_row == 1
                            and abs(end_col - start_col) == 1
                            and self.board[end_row][end_col]
                            and self.board[end_row][end_col].color == 'Black'
                    ):
                        return True, None
                else:                                                                                               #Jeżeli nie jest to pierszy ruch
                    if end_row - start_row == 1 and start_col == end_col and not self.board[end_row][end_col]:      #zwykły ruch o jeden w górę
                        return True, None
                    elif (                                                                                          #Czy jest czarna figura możliwa do zbicia po skosie o jedno pole
                            end_row - start_row == 1
                            and abs(end_col - start_col) == 1
                            and self.board[end_row][end_col]
                            and self.board[end_row][end_col].color == 'Black'
                    ):
                        return True, None
                    elif (                                                                                          #Bicie w przelocie
                            end_row - start_row == 1
                            and abs(end_col - start_col) == 1
                            and start_row == 4
                            and end_row == en_passant[0]
                            and end_col == en_passant[1]

                    ):
                        self.board[end_row-1][end_col] = ''                                                         #Usunięcie zbitego w przelocie pionka
                        return True, None
            else:
                # Logika dla pionka czarnego
                if start_row == 6:
                    if start_row - end_row in (1, 2) and start_col == end_col and not self.board[end_row][end_col]: #Jeżeli to pierwszy ruch białego i ruszył się o jedno lub dwa pola do przodu
                        if (start_row - end_row) == 2:                                                              #dodatkowo jeżeli ruszył się o 2, to może zostać zbity w przelocie
                            en_passant = [end_row+1, end_col]
                        return True, en_passant
                    elif (                                                                                          #Czy jest biała figura możliwa do zbicia po skosie o jedno pole
                            start_row - end_row == 1
                            and abs(end_col - start_col) == 1
                            and self.board[end_row][end_col]
                            and self.board[end_row][end_col].color == 'White'
                    ):
                        return True, None
                else:                                                                                               #Jeżeli nie jest to pierszy ruch
                    if start_row - end_row == 1 and start_col == end_col and not self.board[end_row][end_col]:      #zwykły ruch o jeden w górę
                        return True, None
                    elif (                                                                                          #Czy jest biała figura możliwa do zbicia po skosie o jedno pole
                            start_row - end_row == 1
                            and abs(end_col - start_col) == 1
                            and self.board[end_row][end_col]
                            and self.board[end_row][end_col].color == 'White'
                    ):
                        return True, None
                    elif (                                                                                          #Bicie w przelocie
                            start_row - end_row == 1
                            and abs(end_col - start_col) == 1
                            and start_row == 3
                            and end_row == en_passant[0]
                            and end_col == en_passant[1]
                    ):
                        self.board[end_row + 1][end_col] = ''                                                       #Usunięcie zbitego w przelocie pionka
                        return True, None
        elif isinstance(piece, Knight):
            # Logika dla skoczka
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return (diff_row, diff_col) in [(1, 2), (2, 1)], None
        elif isinstance(piece, Rook):
            # Logika dla wieży
            if start_row == end_row or start_col == end_col:
                return True, None
        elif isinstance(piece, Bishop):
            # Logika dla gońca
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return diff_row == diff_col, None
        elif isinstance(piece, Queen):
            # Logika dla królowej
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return (start_row == end_row or start_col == end_col) or (diff_row == diff_col), None
        elif isinstance(piece, King):
            # Logika dla króla
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return diff_row <= 1 and diff_col <= 1, None
        # Dodaj logikę dla innych pionków
        return False, None


class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        if self.color == 'White':
            return 'p'
        elif self.color == 'Black':
            return 'P'

    def __str__(self):
        return 'Pawn'


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        if self.color == 'White':
            return 'r'
        elif self.color == 'Black':
            return 'R'

    def __str__(self):
        return 'Rook'


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        if self.color == 'White':
            return 'n'
        elif self.color == 'Black':
            return 'N'

    def __str__(self):
        return 'Knight'


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        if self.color == 'White':
            return 'b'
        elif self.color == 'Black':
            return 'B'

    def __str__(self):
        return 'Bishop'


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        if self.color == 'White':
            return 'q'
        elif self.color == 'Black':
            return 'Q'

    def __str__(self):
        return 'Queen'


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def __repr__(self):
        if self.color == 'White':
            return 'k'
        elif self.color == 'Black':
            return 'K'

    def __str__(self):
        return 'King'


# Użycie klas
if __name__ == '__main__':
    chessboard = Chessboard()
    chessboard.startgame()
    chessboard.print_board()
    is_white_turn = True
    en_passant = None

    continue_game = True
    while continue_game:
        if is_white_turn:
            print("White turn")
        else:
            print("Black turn")
        print(en_passant)
        start_row = int(input("Enter start row: "))
        start_col = int(input("Enter start column: "))
        end_row = int(input("Enter end row: "))
        end_col = int(input("Enter end column: "))
        is_white_turn, en_passant = chessboard.move_piece(is_white_turn, en_passant, start_row, start_col, end_row, end_col)
        chessboard.print_board()
        continue_game_input = input("Continue the game? (y/n): ")
        if continue_game_input.lower() != 'y':
            continue_game = False
