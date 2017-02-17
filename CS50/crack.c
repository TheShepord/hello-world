#include <stdio.h>
#include <stdlib.h>
#include <crypt.h>
#include <string.h>

void saltCycle(char *c);
void keyCycle(char *c, char *start);
static int keyLen = 5;

int main(int argc, char *argv[])
{
//    printf("%s\n",(char *) crypt("LOL","aa"));
    if (argc != 2) {
        printf("Usage: ./crack hash");
        return 1;
    }
    char *key = calloc(keyLen,sizeof(char));
    char salt[] = "aa";
    char *hash = argv[1];

    *key = 'a';

    char *res = crypt(key,salt);
    while (strcmp(hash,res) != 0) {
        saltCycle((char *) salt + 1);    //same as saltCycle(&salt[1]);

        if (salt[1] ==  'a') {
            saltCycle((char *) salt);
            if (salt[0] == 'a') {
                keyCycle(key,key);
            }
        }
        res = crypt(key,salt);

        if (strcmp(key,"ZZZZZ") == 0 && strcmp(salt,"//") == 0) {
            printf("error\n");
            return 2;
        }
    }
    printf("%s\n",key);
    free(key);

    return 0;
}


void saltCycle(char *c) {
    if (*c == 'z') {
        *c = 'A';
    }
    else if (*c == 'Z') {
        *c = '0';
    }

    else if (*c == '9') {
        *c = '.';
    }

    else if (*c == '/') {
        *c = 'a';

    }
    else {
        *c = *c + 1;
    }
}

void keyCycle(char *c, char *start) {

    if (*c == '\0') {
        *c = 'a';
    }

    else if (*c == 'z') {
        *c = 'A';
    }
    else if (*c == 'Z') {
        *c = 'a';
        if (c - start < keyLen) {
            keyCycle(c+1, start);
        }
    }
    else {
        *c = *c + 1;
    }
}
