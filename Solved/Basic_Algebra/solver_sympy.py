from sympy import *

eqn = '''
flag[0] + flag[1] == 231
flag[1] + flag[2] == 233
flag[2] + flag[3] == 235
flag[3] + flag[4] == 190
flag[4] + flag[5] == 115
flag[5] + flag[6] == 125
flag[6] + flag[7] == 157
flag[7] + flag[8] == 165
flag[8] + flag[9] == 140
flag[9] + flag[10] == 160
flag[10] + flag[11] == 183
flag[11] + flag[12] == 149
flag[12] + flag[13] == 166
flag[13] + flag[14] == 172
flag[14] + flag[15] == 129
flag[15] + flag[16] == 136
flag[16] + flag[17] == 156
flag[17] + flag[18] == 105
flag[18] + flag[19] == 158
flag[19] + flag[20] == 135
flag[20] + flag[0] == 120
'''.strip()

# in sympy, equations equate to zero
eqn = eqn.replace('==', '-')

# replace with brackets to allow for easy sorting
eqn = eqn.replace('[', '(')
eqn = eqn.replace(']', ')')
solution = solve(eqn.splitlines())[0]
print(solution)

# retrieve values of ascii codes
ascii_codes = list(solution.values())
print(ascii_codes)

# convert ascii codes to ascii chars
flag = list(map(chr, ascii_codes))
flag = ''.join(flag)
print(flag)
