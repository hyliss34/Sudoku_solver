# Sudoku solver

This a 'full' sudoku solver that uses opencv and tesseract for extracting the sudoku grid from an image and then pulp for solving the sudoku.

To install just do:

```bash
pip install -r requirements.txt
```

Then run the solver on the sudoku you want to solve

```
python -m sudoku_solver.Solve 'file.png' 
```
You can set the output file name

```
python -m sudoku_solver.Solve 'file.png' outputfilename
```
For more infos you can typee

```
python -m sudoku_solver.Solve --help

```