# Sudoku solver

This a 'full' sudoku solver that uses opencv and tesseract for extracting the sudoku grid from an image and then pulp for solving the sudoku.

To install just do:

```bash
pip install -r requirements.txt
```

Then run the solver on the sudoku you want to solve

```
python Solve.py 'file.png'
```
You can set the output file name

```
python Solve.py 'file.png' outputfilename
```
For more infos you can type

```
python Solve.py --help
```