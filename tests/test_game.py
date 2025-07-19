from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_no_word_input_is_invalid(self):
            # setup
            new_game = Game()

            # verify
            assert new_game.is_valid('') is False

    def test_word_input_is_valid(self):
            # setup
            new_game = Game()
            test_grid = 'MATHGOLDS'
            test_word = 'MOTHS'

            #exercise
            new_game.grid = list(test_grid)

            # verify
            assert new_game.is_valid(test_word) is True

            # teardown
            assert new_game.grid == list(test_grid)

    def test_word_input_is_invalid(self):
            # setup
            new_game = Game()
            test_grid = 'MATHGOLDS'
            test_word = 'SCIENCE'

            # exercise
            new_game.grid = list(test_grid)

            # verify
            assert new_game.is_valid(test_word) is False

            # teardown
            assert new_game.grid == list(test_grid)
