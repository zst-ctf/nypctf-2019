# Clean up my mess!
Misc

## Challenge 

	Description
	Special Agent Fox Mulder seems to have spilled coffee on an important file and is unable to access it. Can you help him clean up and open the file up for him? 

	Author Ravin

	Value
	400


## Solution

PDF file

	$ file flag.docx 
	flag.docx: PDF document, version 1.7

	$ xxd flag.docx 
	00000000: 2550 4446 2d31 2e37 0d25 e2e3 cfd3 0d0a  %PDF-1.7.%......
	00000010: 3134 2030 206f 626a 0d3c 3c2f 4c69 6e65  14 0 obj.<</Line

Rename it to .pdf and open it.

There is a password

https://netlockit.wordpress.com/2017/11/03/cracking-password-protected-pdf-files-with-john-the-ripper/

	$ /usr/local/Cellar/john-jumbo/1.8.0/share/john/pdf2john.py flag.pdf 
	flag.pdf:$pdf$4*4*128*-1028*1*16*b03a99ae5e37ad43a483da257cfafe37*:::::flag.pdf
	
???


	/usr/local/Cellar/john-jumbo/1.8.0/share/john/john flag.pdf --format=PDF --wordlist=~/rockyou.txt

## Flag

	??