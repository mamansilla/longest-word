'''
Word Grid Game Module

This module defines a simple word validation game. It generates a random 3x3 grid
(9 letters total) of uppercase letters. A user can then input a word, and the game
validates whether the word can be formed from the letters in the grid, using each
letter no more times than it appears.

Classes:
    Game: Handles grid generation and word validation logic.
'''

import string
import random
import requests

class Game:
    '''
    A simple word validation game using a 3x3 grid of random uppercase letters.

    Attributes:
        grid (list of str): A list containing 9 randomly selected uppercase letters.
    '''
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        grid_list = list(self.grid)
        for char in word:
            if char in grid_list:
                grid_list.remove(char)
            else:
                return False
        return True

    def is_valid(self, word):
        # [...]

        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']

    def get_grid(self) -> list:
        """Return the current grid"""
        return self.grid
