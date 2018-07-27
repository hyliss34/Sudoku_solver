from Digits_extractor import get_board
from Solver import  solve_sudoku

sudoku = get_board("sudoku.png")
solve_sudoku(sudoku)
