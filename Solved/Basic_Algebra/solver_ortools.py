#!/usr/bin/env python3
from ortools.sat.python import cp_model

# Create model.
model = cp_model.CpModel()

# Create integer variables for flag
flag_size = 25
flag = [model.NewIntVar(0, 2**8, f'x_{i}') for i in range(flag_size)]

# Add solver constraints
model.Add(flag[0] + flag[1] == 231)
model.Add(flag[1] + flag[2] == 233)
model.Add(flag[2] + flag[3] == 235)
model.Add(flag[3] + flag[4] == 190)
model.Add(flag[4] + flag[5] == 115)
model.Add(flag[5] + flag[6] == 125)
model.Add(flag[6] + flag[7] == 157)
model.Add(flag[7] + flag[8] == 165)
model.Add(flag[8] + flag[9] == 140)
model.Add(flag[9] + flag[10] == 160)
model.Add(flag[10] + flag[11] == 183)
model.Add(flag[11] + flag[12] == 149)
model.Add(flag[12] + flag[13] == 166)
model.Add(flag[13] + flag[14] == 172)
model.Add(flag[14] + flag[15] == 129)
model.Add(flag[15] + flag[16] == 136)
model.Add(flag[16] + flag[17] == 156)
model.Add(flag[17] + flag[18] == 105)
model.Add(flag[18] + flag[19] == 158)
model.Add(flag[19] + flag[20] == 135)
model.Add(flag[20] + flag[0] == 120)

# Creates a solver and solves the model.
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
    # Convert to char and print to screen
    for i in range(flag_size):
        value = solver.Value(flag[i])
        char = chr(value)
        print(char, end='')
    print('')
