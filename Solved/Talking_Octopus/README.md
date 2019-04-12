# Talking Octopus
Misc

## Challenge 

	Description
	Bloop Bloop, here comes my 8 tentacles 

	Author: Syahiran

	Value
	100

	116 131 120 173 115 122 056 117 103 124 101 114 120 125 123 175

## Solution

Octal to ASCII

Ruby script

	seq = '116 131 120 173 115 122 056 117 103 124 101 114 120 125 123 175'
	chars = seq.split(' ').map { |x| x.to_i(8).chr }
	chars.join ''
	=> "NYP{MR.OCTALPUS}"

## Flag

	NYP{MR.OCTALPUS}
