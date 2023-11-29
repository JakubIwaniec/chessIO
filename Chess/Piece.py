class Piece:
    def __init__(self, color):
        self.color = color
        self.path_to_image = None


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'White':
            self.path_to_image = 'Images\\FigureSkins\\wP.jpg'
        elif self.color == 'Black':
            self.path_to_image = 'Images\\FigureSkins\\bP.jpg'

    def __repr__(self):
        if self.color == 'White':
            return 'p'
        elif self.color == 'Black':
            return 'P'

    def __str__(self):
        return 'Pawn'


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'White':
            self.path_to_image = 'Images\\FigureSkins\\wR.jpg'
        elif self.color == 'Black':
            self.path_to_image = 'Images\\FigureSkins\\bR.jpg'

    def __repr__(self):
        if self.color == 'White':
            return 'r'
        elif self.color == 'Black':
            return 'R'

    def __str__(self):
        return 'Rook'


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'White':
            self.path_to_image = 'Images\\FigureSkins\\wN.jpg'
        elif self.color == 'Black':
            self.path_to_image = 'Images\\FigureSkins\\bN.jpg'

    def __repr__(self):
        if self.color == 'White':
            return 'n'
        elif self.color == 'Black':
            return 'N'

    def __str__(self):
        return 'Knight'


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'White':
            self.path_to_image = 'Images\\FigureSkins\\wB.jpg'
        elif self.color == 'Black':
            self.path_to_image = 'Images\\FigureSkins\\bB.jpg'

    def __repr__(self):
        if self.color == 'White':
            return 'b'
        elif self.color == 'Black':
            return 'B'

    def __str__(self):
        return 'Bishop'


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'White':
            self.path_to_image = 'Images\\FigureSkins\\wQ.jpg'
        elif self.color == 'Black':
            self.path_to_image = 'Images\\FigureSkins\\bQ.jpg'

    def __repr__(self):
        if self.color == 'White':
            return 'q'
        elif self.color == 'Black':
            return 'Q'

    def __str__(self):
        return 'Queen'


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'White':
            self.path_to_image = 'Images\\FigureSkins\\wK.jpg'
        elif self.color == 'Black':
            self.path_to_image = 'Images\\FigureSkins\\bK.jpg'

    def __repr__(self):
        if self.color == 'White':
            return 'k'
        elif self.color == 'Black':
            return 'K'

    def __str__(self):
        return 'King'