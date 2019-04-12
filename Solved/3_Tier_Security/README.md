# 3-Tier Security
Crypto

## Challenge 

	Description
	Special Agent Fox Mulder has intercepted a peculiar message but it seems to be encrypted strongly. Can you help out our agent to decrypt the message? 
	Note: Flag submission should be in lowercase ( e.g. NYP{abc_123_def} ) 

	Author: Ravin
	
	Value
	350

> [transmission.wav](transmission.wav)

## Solution

We hear morse code

I wrote a script in Ruby to parse it.

We get the text

	github.com/ravin-d

Visit the page and we see this file

https://github.com/ravin-d/NYP-Infosec/blob/master/flag.txt

Apparently it is ROT13.

After putting it through ROT13, we see some lorum ipsum text with some capitals, numbers and underscores.

Remove the lowercase and we get the flag

	$ python3 -c "import codecs, re; print(re.sub('[a-z ,|]', '', codecs.encode( open('flag.txt').read(), 'rot13')).lower())"
	4ut0mat10n_w4s_th3_0nly_w4y_t0_g0_4_th1s_200x200s200lq2004x

## Flag

	NYP{4ut0mat10n_w4s_th3_0nly_w4y_t0_g0_4_th1s_200x200s200lq2004x}
