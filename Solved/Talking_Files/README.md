# Talking Files
Misc

## Challenge 

	Description
	Going strong so far, how about this? Thou is an art, thy shall see I when the can’t see ASCII Characters in files 

	Author: Syahiran

	Value
	75

	4e 59 50 7b 54 68 33 5f 46 21 6c 33 5f 53 70 33 61 6b 73 7d

## Solution

Convert hex to ASCII in Bash

	$ STR='4e 59 50 7b 54 68 33 5f 46 21 6c 33 5f 53 70 33 61 6b 73 7d'
	$ echo $STR | tr -d ' ' | xxd -r -p
	NYP{Th3_F!l3_Sp3aks}
