#include <stdio.h>

// Given the equation, if we know the first
// character flag[0], we can solve the flag[1]

// Rearranging the equation: 
// -> flag[0] + flag[1] == 231
// -> flag[1] = 231 - flag[0];

// Likewise, if we know the flag[1], we can solve for flag[2]
// -> flag[2] = 233 - flag[1];

// Hence, we can simply bruteforce the first character of the flag
// and then calculate the rest.

char flag[21];
void calculate(char start){
    flag[0] = start;
    flag[1] = 231 - flag[0];
    flag[2] = 233 - flag[1];
    flag[3] = 235 - flag[2];
    flag[4] = 190 - flag[3];
    flag[5] = 115 - flag[4];
    flag[6] = 125 - flag[5];
    flag[7] = 157 - flag[6];
    flag[8] = 165 - flag[7];
    flag[9] = 140 - flag[8];
    flag[10] = 160 - flag[9];
    flag[11] = 183 - flag[10];
    flag[12] = 149 - flag[11];
    flag[13] = 166 - flag[12];
    flag[14] = 172 - flag[13];
    flag[15] = 129 - flag[14];
    flag[16] = 136 - flag[15];
    flag[17] = 156 - flag[16];
    flag[18] = 105 - flag[17];
    flag[19] = 158 - flag[18];
    flag[20] = 135 - flag[19];
    flag[0] = 120 - flag[20];
    printf("Try %d: %s\n", start, flag);
}

int main(){
    for (int x = 0; x < 128; x++) {
        calculate(x);
    }
    return 0;
}
