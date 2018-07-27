import sys
from solver.Solve import solve

file = sys.argv[1]
output = sys.argv[2]
print(output)

solve(file, output)