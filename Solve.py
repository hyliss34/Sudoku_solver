from solver.Solver import solve_sudoku
from extractor.Digits_extractor import get_board
import sys



def main():


    try:
        file = sys.argv[1]
    except Exception:
        raise Exception("A file name is needed !")

    if file == "--help":
        print("""Usage: Solve.py filename outputname(optionnal)
        filename is required
        outputname is just a name without file extension, if blank the files will be named 'sudokusolution'""")
        return
    else:
        sudoku = get_board(file)

    try:
        output = sys.argv[2]
        solve_sudoku(sudoku, output)
    except Exception :
        solve_sudoku(sudoku)


#def solve(file, output="sudokusolution"):
#    sudoku = get_board(file)
#    solve_sudoku(sudoku, output)

main()