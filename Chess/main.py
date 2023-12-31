from Chess.Piece import *


class Chessboard:
    def __init__(self):
        self.board = [['' for _ in range(8)] for _ in range(8)]

    @classmethod
    def startgame(cls, target_board) -> None:
        white_rookA = Rook('White')
        target_board.place_piece(white_rookA, 0, 0)

        white_knightA = Knight('White')
        target_board.place_piece(white_knightA, 0, 1)

        white_bishopB = Bishop('White')
        target_board.place_piece(white_bishopB, 0, 2)

        white_queen = Queen('White')
        target_board.place_piece(white_queen, 0, 3)

        white_king = King('White')
        target_board.place_piece(white_king, 0, 4)

        white_bishopW = Bishop('White')
        target_board.place_piece(white_bishopW, 0, 5)

        white_knightB = Knight('White')
        target_board.place_piece(white_knightB, 0, 6)

        white_rookB = Rook('White')
        target_board.place_piece(white_rookB, 0, 7)

        for x in range(8):
            white_pawn = Pawn('White')
            target_board.place_piece(white_pawn, 1, x)

        for x in range(8):
            black_pawn = Pawn('Black')
            target_board.place_piece(black_pawn, 6, x)

        black_rookA = Rook('Black')
        target_board.place_piece(black_rookA, 7, 0)

        black_knightA = Knight('Black')
        target_board.place_piece(black_knightA, 7, 1)

        black_bishopW = Bishop('Black')
        target_board.place_piece(black_bishopW, 7, 2)

        black_queen = Queen('Black')
        target_board.place_piece(black_queen, 7, 3)

        black_king = King('Black')
        target_board.place_piece(black_king, 7, 4)

        black_bishopB = Bishop('Black')
        target_board.place_piece(black_bishopB, 7, 5)

        black_knightB = Knight('Black')
        target_board.place_piece(black_knightB, 7, 6)

        black_rookB = Rook('Black')
        target_board.place_piece(black_rookB, 7, 7)

    def print_board(self):
        for row in self.board:
            print(row)

    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def is_clear_path(self, start_row, start_col, end_row, end_col):
        # Sprawdzanie czy ścieżka między dwoma polami jest pusta
        diff_row = end_row - start_row
        diff_col = end_col - start_col

        # Sprawdź kierunek ruchu i odpowiednią oś
        if diff_row == 0:
            step = 1 if diff_col > 0 else -1
            for col in range(start_col + step, end_col, step):
                if self.board[start_row][col]:
                    return False
        elif diff_col == 0:
            step = 1 if diff_row > 0 else -1
            for row in range(start_row + step, end_row, step):
                if self.board[row][start_col]:
                    return False
        else:
            step_row = 1 if diff_row > 0 else -1
            step_col = 1 if diff_col > 0 else -1
            row, col = start_row + step_row, start_col + step_col
            while row != end_row and col != end_col:
                if self.board[row][col]:
                    return False
                row += step_row
                col += step_col

        return True

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

            # Ustawienie has_moved dla króla i wieży po roszadzie
            if isinstance(piece, King):
                piece.has_moved = True
                if end_col - start_col == 2:  # Roszada krótka (w prawo)
                    rook = self.board[end_row][end_col - 1]
                    rook.has_moved = True
                elif start_col - end_col == 2:  # Roszada długa (w lewo)
                    rook = self.board[end_row][end_col + 1]
                    rook.has_moved = True

            elif isinstance(piece, Rook):
                piece.has_moved = True

            if isinstance(piece, Pawn) and (end_row == 0 or end_row == 7):
                promotion_choice = input("Choose the promotion piece (Rook, Knight, Bishop, or Queen): ")
                promoted_piece = None

                # Stwórz instancję wybranej figury na podstawie wyboru gracza
                if promotion_choice.lower() == 'rook':
                    promoted_piece = Rook(piece.color)
                elif promotion_choice.lower() == 'knight':
                    promoted_piece = Knight(piece.color)
                elif promotion_choice.lower() == 'bishop':
                    promoted_piece = Bishop(piece.color)
                elif promotion_choice.lower() == 'queen':
                    promoted_piece = Queen(piece.color)

                # Zamień piona na wybraną figurę
                if promoted_piece:
                    self.board[end_row][end_col] = promoted_piece
                else:
                    print("Invalid promotion choice. Defaulting to Queen.")
                    self.board[end_row][end_col] = Queen(piece.color)

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
                return self.is_clear_path(start_row, start_col, end_row, end_col), None
        elif isinstance(piece, Bishop):
            # Logika dla gońca
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return self.is_clear_path(start_row, start_col, end_row, end_col) and diff_row == diff_col, None
        elif isinstance(piece, Queen):
            # Logika dla królowej
            diff_row = abs(end_row - start_row)
            diff_col = abs(end_col - start_col)
            return self.is_clear_path(start_row, start_col, end_row, end_col) and (start_row == end_row or start_col == end_col or diff_row == diff_col), None
        elif isinstance(piece, King):
            # Logika dla króla
                # Warunki dla roszady
                if not piece.has_moved and end_col - start_col == 2:  # Roszada krótka (w prawo)
                    if (
                            not self.board[start_row][start_col + 1]
                            and not self.board[start_row][start_col + 2]
                            and isinstance(self.board[start_row][start_col + 3], Rook)
                            and not self.board[start_row][start_col + 3].has_moved
                    ):
                        rook = self.board[start_row][start_col + 3]
                        self.board[end_row][end_col - 1] = rook
                        self.board[start_row][start_col + 3] = ''
                        rook.position = (end_row, end_col - 1)

                        return True, None

                elif not piece.has_moved and start_col - end_col == 2:  # Roszada długa (w lewo)
                    if (
                            not self.board[start_row][start_col - 1]
                            and not self.board[start_row][start_col - 2]
                            and not self.board[start_row][start_col - 3]
                            and isinstance(self.board[start_row][start_col - 4], Rook)
                            and not self.board[start_row][start_col - 4].has_moved
                    ):
                        rook = self.board[start_row][start_col - 4]
                        self.board[end_row][end_col + 1] = rook
                        self.board[start_row][start_col - 4] = ''
                        rook.position = (end_row, end_col + 1)
                        return True, None
                else:
                    diff_row = abs(end_row - start_row)
                    diff_col = abs(end_col - start_col)
                    return diff_row <= 1 and diff_col <= 1, None
        return False, None

def is_white_king_on_board(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if isinstance(piece, King) and piece.color == 'White':
                return True
    return False
def is_black_king_on_board(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if isinstance(piece, King) and piece.color == 'Black':
                return True
    return False

# Użycie klas
if __name__ == '__main__':
    chessboard = Chessboard()
    Chessboard.startgame(chessboard)
    chessboard.print_board()
    is_white_turn = True
    en_passant = None

    continue_game = True

    while continue_game:
        if is_white_turn:
            print("White turn")
        else:
            print("Black turn")
        start_row = int(input("Enter start row: "))
        start_col = int(input("Enter start column: "))
        end_row = int(input("Enter end row: "))
        end_col = int(input("Enter end column: "))
        is_white_turn, en_passant = chessboard.move_piece(is_white_turn, en_passant, start_row, start_col, end_row, end_col)
        chessboard.print_board()
        if not is_white_king_on_board(chessboard.board):
            print("Czarne wygrały")
            break
        elif not is_black_king_on_board(chessboard.board):
            print("Białe wygrały")
            break
        continue_game_input = input("Continue the game? (y/n): ")
        if continue_game_input.lower() != 'y':
            continue_game = False
