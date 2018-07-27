import unittest
import os

import solver
import extractor.Digits_extractor

class TestWorkingSudokus(unittest.TestCase):

    def test_full(self):
        path = 'examples_boards/working/'
        files = os.listdir(path)
        for file in files:
            sudoku = extractor.Digits_extractor.get_board(path+file)
            is_good = solver.Solve.solve_sudoku(sudoku)
            self.assertTrue(is_good)


if __name__ == '__main__':
    unittest.main()