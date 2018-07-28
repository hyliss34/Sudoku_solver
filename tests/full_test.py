import unittest
from sudoku_solver import Solver, Digits_extractor
import os

class TestWorkingSudokus(unittest.TestCase):

    def test_full(self):
        files = os.listdir('examples_boards/working/')
        for file in files:
            good = Solver.solve_sudoku(Digits_extractor.get_board('examples_boards/working/'+str(file)))
        self.assertTrue(good)

if __name__ == '__main__':
    unittest.main()