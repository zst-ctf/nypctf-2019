import random

print('''I heard some of you are good in computing math. Do you like some simultaneous equations?

Let's have an example. We are given some equations.
    example[0] + example[1] == 195
    example[1] + example[2] == 197
    example[2] + example[0] == 196

Using simultaneous equations, we can solve it to get 'abc'
    example[0] = 97 = 'a'
    example[1] = 98 = 'b'
    example[2] = 99 = 'c'
''')

# read flag into variable
with open("flag.txt") as f:
    flag = f.read()

flag_len = len(flag)

# convert string into array of ASCII integers
flag = list(map(ord, flag))

print()
print(f"Now, for the real deal. Good luck!.")
print(f"The flag is {flag_len} characters long (ie. index 0 through {flag_len-1}).")

# create equations
for i in range(flag_len):
    # choose 2 index of the flag
    # then get result of the equation
    a = i
    b = (i+1) % flag_len  # modulo to make it wrap back to beginning
    result = flag[a] + flag[b]
    print(f"    flag[{a}] + flag[{b}] == {result}")

'''
# Harder version using random index
for i in range(flag_len):
    a = random.randint(0, flag_len-1)
    b = random.randint(0, flag_len-1)
    c = random.randint(0, flag_len-1)
    result = flag[a] + flag[b] + flag[c]
    print(f"    flag[{a}] + flag[{b}] + flag[{c}] == {result}")
    # print(f"    flag[{a}] + flag[{b}] == {result}")
'''
