# Talking Computers
Misc

## Challenge 

	Description
	Hello there, we have taken an interest in you. Complete our trials to join us. This is pretty obvious, what language does a computer speak? 

	Author: Syahiran
	
	Value
	75

	01001110 01011001 01010000 01111011 01000010 00110001 01001110 00110100 01010010 01011001 01011111 00100001 01010011 01011111 01000011 00110000 00110000 01001100 01111101

## Solution

Binary to ASCII

Ruby script

	seq = '01001110 01011001 01010000 01111011 01000010 00110001 01001110 00110100 01010010 01011001 01011111 00100001 01010011 01011111 01000011 00110000 00110000 01001100 01111101'
	chars = seq.split(' ').map { |str| str.to_i(2).chr }
	chars.join('')

	=> "NYP{B1N4RY_!S_C00L}"

## Flag

	NYP{B1N4RY_!S_C00L}