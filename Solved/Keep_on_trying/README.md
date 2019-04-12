# Keep on trying
Crypto

## Challenge 

    Description
    \KBiJ]@MP@GFWMT"@QWM#AMTG\o 

    Add hint: Coffee, tea or flag? 

    Author: Hugo
    Value
    100

## Solution

XOR Cipher

Cycle through 0 through 255 as the key

```python
from itertools import cycle
def bxor(a1, b1):
    encrypted = [ (a ^ b) for (a, b) in zip(a1, b1) ]
    return bytes(encrypted)

for i in range(256):
    decoded = (bxor(b'\KBiJ]@MP@GFWMT"@QWM#AMTG\o ', cycle(bytes([i]))))
    if b'NYP' in decoded: print(i, decoded)
```

18 b'NYP{XOR_BRUTE_F0RCE_1S_FUN}2'


## Flag

    NYP{XOR_BRUTE_F0RCE_1S_FUN}

    