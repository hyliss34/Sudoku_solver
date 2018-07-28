
# Import PuLP modeler functions
from pulp import *
import pprint
import os
import numpy as np
from . import Draw_png

def solve_sudoku(img, output_name = "sudokusolution", output_path = 'output/'):
    """

    :param output_name:
    :param img: an image grayscale
    :type img: np.ndarray
    :return: Two files
        - Sudoku.lp containing the choice made for the resolution
        - sudokouout.txt the solved grid
    """
    # A list of strings from "1" to "9" is created
    Sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # The Vals, Rows and Cols sequences all follow this form
    Vals = Sequence
    Rows = Sequence
    Cols = Sequence

    # The boxes list is created, with the row and column index of each square in each box
    Boxes = []
    for i in range(3):
        for j in range(3):
            Boxes += [[(Rows[3 * i + k], Cols[3 * j + l]) for k in range(3) for l in range(3)]]

    # The prob variable is created to contain the problem data
    prob = LpProblem("Sudoku Problem", LpMinimize)

    # The problem variables are created
    choices = LpVariable.dicts("Choice", (Vals, Rows, Cols), 0, 1, LpInteger)

    # The arbitrary objective function is added
    prob += 0, "Arbitrary Objective Function"

    # A constraint ensuring that only one value can be in each square is created
    for r in Rows:
        for c in Cols:
            prob += lpSum([choices[v][r][c] for v in Vals]) == 1, ""

    # The row, column and box constraints are added for each value
    for v in Vals:
        for r in Rows:
            prob += lpSum([choices[v][r][c] for c in Cols]) == 1, ""

        for c in Cols:
            prob += lpSum([choices[v][r][c] for r in Rows]) == 1, ""

        for b in Boxes:
            prob += lpSum([choices[v][r][c] for (r, c) in b]) == 1, ""

    # The starting numbers are entered as constraints
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] != 0:
                try:
                    prob += choices[str(img[i, j])][str(i+1)][str(j+1)] == 1
                except KeyError as ke:
                    print(i,j, img[i,j])
                    raise ke

    # The problem data is written to an .lp file
    if os.path.exists(output_path+'logs'):
        prob.writeLP(output_path+"logs/Sudoku.lp")
    else:
        os.mkdir(output_path)
        os.mkdir(output_path+'/logs')
        prob.writeLP(output_path+"logs/Sudoku.lp")

    data = np.empty((9, 9), dtype=int)


    sudokuout = open(output_path+output_name+'.txt', 'w')

    for i in range(50):
        prob.solve()
        # The status of the solution is printed to the screen
        print("Status:", LpStatus[prob.status])
        # The solution is printed if it was deemed "optimal" i.e met the constraints
        if LpStatus[prob.status] == "Optimal":
            # The solution is written to the sudokuout.txt file
            for r in Rows:
                if r == "1" or r == "4" or r == "7":
                    sudokuout.write("+-------+-------+-------+\n")
                for c in Cols:
                    for v in Vals:
                        if value(choices[v][r][c]) == 1:
                            if c == "1" or c == "4" or c == "7":
                                sudokuout.write("| ")
                            sudokuout.write(v + " ")
                            data[int(r)-1, int(c)-1] = int(v)
                            if c == "9":
                                sudokuout.write("|\n")
            sudokuout.write("+-------+-------+-------+\n\n")
            return True
        else:
            prob += lpSum([choices[v][r][c] for v in Vals
                           for r in Rows
                           for c in Cols
                           if value(choices[v][r][c]) == 1]) <= 80
    return False
    sudokuout.close()
    Draw_png.construct_grid_image(data, output_path+output_name + ".png")
    # The location of the solutions is give to the user
    print("Solutions Written to " + output_name + ".txt and " + output_name + ".png")

