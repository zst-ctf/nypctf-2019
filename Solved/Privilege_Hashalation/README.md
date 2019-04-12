# Privilege Hashalation
Crypto

## Challenge 

	Description
	We were able to gain access into Agent Bain's Machine. However, it seems that we’ll need to escalate privilege on the machine to extract the files from the machine. Will you be able to get the root’s password of the machine from this hashed password file. 

	Author: Syahiran

	Value
	250

## Solution

John-the-Ripper to crack the shadow file.

Using john-jumbo on Mac

	$ /usr/local/Cellar/john-jumbo/1.8.0/share/john/john shadow.txt 

	starwars         (root)

## Flag

	NYP{starwars}
