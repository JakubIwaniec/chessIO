"""
25/10
Skrypt opisuje zachowanie SI (sztucznej inteligencji)
"""

from abc import ABCMeta, abstractmethod
import Chess.main


class Bots(metaclass=ABCMeta):
    @abstractmethod
    def evaluate_function(self):
        """
        Ta funkcja ma określać sposób
        oceniania figur.
        :return:
        """
        pass

    @abstractmethod
    def scoring_function(self, piece: Chess.main.Piece) -> int:
        """
        Ta funkcja ma przedstawiać sposób
        punktowania figur - własnych i przeciwnika
        i zwracać wynik dla konkretnego pionu.
        :return:
        """
        pass

    @staticmethod
    def all_possible_moves(board: list, depth: int) -> list:
        """
        Ta funkcja ma zwracać przestrzeń możliwych ruchów
        do określonej głębokości.
        :param board:
        :param depth:
        :return:
        """
        assert type(board) is list
        assert type(depth) is int and depth > 0
        return []
