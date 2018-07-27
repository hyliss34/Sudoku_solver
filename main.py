from Digits_extractor import get_board
from Solver import  solve_sudoku

sudoku = get_board("examples_boards/working/sudoku-original.jpg")
solve_sudoku(sudoku)
