# What's that gibberish?
Misc

## Challenge 

	Description
	Agent Dana Scully seemed to have picked up some unknown documents from dumpster diving. Can you make sense of it? 

	Author: Hugo
	Value
	250


## Solution

We see base64, and upon decoding, we get hex. 
	
	$ cat flag.txt | base64 --decode | xxd -r -p > decoded

Now the decoded output is some binary file. Check its type

	$ file decoded 
	decoded: gzip compressed data, was "flag.txt", last modified: Mon Mar 25 13:12:43 2019, from Unix

Use gunzip to get flag.txt

	$ gunzip < decoded > final

## Flag

	NYP{Mult1ple_Enc0d1ng_1s_n0t_Ea5y}
