import unittest
import os

from solver.Solver import solve_sudoku
from extractor.Digits_extractor import get_board

class TestWorkingSudokus(unittest.TestCase):

    def test_full(self):
        path = 'examples_boards/working/'
        #files = os.listdir(path)
        #for file in files:
        sudoku = get_board(path+"sudoku-original.jpg")
        is_good = solve_sudoku(sudoku)
        print(is_good)
        #self.assertTrue(is_good)


if __name__ == '__main__':
    unittest.main()