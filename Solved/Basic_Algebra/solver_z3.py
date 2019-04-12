#!/usr/bin/env python3
# export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin
# export PYTHONPATH=~/Downloads/z3-4.8.0.99339798ee98-x64-osx-10.11.6/bin/python
from z3 import *

# create integer variables for flag
flag_size = 25
flag = IntVector("flag", flag_size)

# add solver constraints
s = Solver()
s.add(flag[0] + flag[1] == 231)
s.add(flag[1] + flag[2] == 233)
s.add(flag[2] + flag[3] == 235)
s.add(flag[3] + flag[4] == 190)
s.add(flag[4] + flag[5] == 115)
s.add(flag[5] + flag[6] == 125)
s.add(flag[6] + flag[7] == 157)
s.add(flag[7] + flag[8] == 165)
s.add(flag[8] + flag[9] == 140)
s.add(flag[9] + flag[10] == 160)
s.add(flag[10] + flag[11] == 183)
s.add(flag[11] + flag[12] == 149)
s.add(flag[12] + flag[13] == 166)
s.add(flag[13] + flag[14] == 172)
s.add(flag[14] + flag[15] == 129)
s.add(flag[15] + flag[16] == 136)
s.add(flag[16] + flag[17] == 156)
s.add(flag[17] + flag[18] == 105)
s.add(flag[18] + flag[19] == 158)
s.add(flag[19] + flag[20] == 135)
s.add(flag[20] + flag[0] == 120)

# check if there is a solution
if s.check() != sat:
    print("No solution")
    quit()

m = s.model()

# convert to int array
flag = [0] * flag_size
for name in m:
    value = m[name]
    index = int(str(name).split('__')[1])

    flag[index] = int(str(value))
    ch = chr(flag[index])
    print(f"{name} at {hex(index)} = {value} {ch}")

# convert to char array or string
flag = ''.join(list(map(lambda x: chr(x) if x else '\x00', flag)))
print('flag =', flag)
print('flag (hex) =', flag.encode().hex())
