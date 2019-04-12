# Basic Algebra
Misc

## Challenge 

An introductory maths challenge which I created.

	Description
	Convert all characters to upper case 

	Author: Manzel
	Value
	200

[challenge.txt](challenge.txt)

## Generate

This is the script to generate the challenge

[generate.py](generate.py)

## Solution

This problem can be solved in a few ways.

### 1. Bruteforce

Given the equation, if we know the first character flag[0], we can solve the flag[1]. Likewise, if we know the flag[1], we can solve for flag[2] and so on...

Hence, we can simply bruteforce the first character of the flag and then calculate the rest.

I implemented a solution in C language.

[solve.c](solve.c)

	// Rearranging the equation: 
	// -> flag[0] + flag[1] == 231
	// -> flag[1] = 231 - flag[0];

	// Likewise, if we know the flag[1], we can solve for flag[2]
	// -> flag[2] = 233 - flag[1];

	// Hence, we can simply bruteforce the first character of the flag
	// and then calculate the rest.

### 2. Constraint Solver

[Microsoft Z3](https://github.com/Z3Prover/z3) can be used to input the equation constraints and solve for a solution.

- [solver_z3.py](solver_z3.py)


[Google OR-Tools](https://developers.google.com/optimization/cp/cp_solver) has a constraint optimization solver too.

- [solver_ortools.py](solver_ortools.py)


### 3. Linear Equation Solver

Python Sympy library is useful for algebra manipulation. It can solve for an array of equations.

[solver_sympy.py](solver_sympy.py)

## Flag

[flag.txt](flag.txt)
