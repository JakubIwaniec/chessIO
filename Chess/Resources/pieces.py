"""
24/11
Skrypt opisuje obiekty szachownicy.
TO DO: usunięcie tutejszej zawartości i wtłoczenie
obiektów z 'main.py'
"""

from abc import ABCMeta, abstractmethod


class PieceType(metaclass=ABCMeta):
    @abstractmethod
    def valid_moves(self):
        pass


class PieceColor:
    def __init__(self, color: str):
        # akceptuj tylko dwie wartości
        if color == 'Black':
            self.color = color
        if color == 'White':
            self.color = color

    def __str__(self):
        return self.color


class Piece:
    def __init__(self, piece_color: PieceColor, piece_position, has_moved: bool):
        self.piece_color = piece_color
        self.piece_position = piece_position
        self.has_moved = has_moved
