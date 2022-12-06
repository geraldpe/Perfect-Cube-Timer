#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void setup() {
    // sets the seed to get different numbers each execution
    time_t t1; 
    srand((unsigned) time (&t1));
}

int getRandomNumber(int max) {
    // donne un nombre random entre 0 et max (utiliser après setup)
    int a = rand() % max;
    return a;
}

void scramble(char *result) {
    // fonction de génération de mélanges
    char FACES[] = "FRULBD";
    char SYMBOLS[] = "' 2";
    int currentNumber = 0;
    int forbiddenNumber = 7;

    for (int i = 0; i < 60 ; i+=3) {
        currentNumber = getRandomNumber(6);
        while (currentNumber == forbiddenNumber) {
                currentNumber = getRandomNumber(6);
        }
        forbiddenNumber = currentNumber;
        result[i] = FACES[currentNumber];
        result[i+1] = SYMBOLS[getRandomNumber(3)];
        result[i+2] = ' ';
    }
}

int main(void) {
    setup();    
    char the_scramble[61];
    for (int i = 0; i<5 ; i++) {
        scramble(the_scramble);
        printf("%s \n", the_scramble);
    }
    return 0;
}