from Solver import solve_sudoku
from Digits_extractor import get_board
import sys


file = sys.argv[1]
sudoku = get_board(file)
solve_sudoku(sudoku)
