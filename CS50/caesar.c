#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int aredigits(string s);
string shift(string s, int key);

int main(int argc, string argv[]) {
 //   char str[argc-1];
 //   memcpy(str,argv[1],argc-1);
   // printf("%i",atoi(argv[1]));

    if (argc==2 && aredigits(argv[1])) {
        int key = atoi(argv[1]);
        string text = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0, n = strlen(text); i < n; i++) {
            if (isupper(text[i])) {
                printf("%c",
                       ((text[i]+key-'A')%26)+'A');  
            }
            else if (islower(text[i])) {
                printf("%c",
                       ((text[i]+key-'a')%26)+'a');
            }
            else {
                printf("%c",text[i]);
            }
            
        }
        printf("\n");
    }

    else {
        printf("Usage: ./caesar key\n");
    }
}

int aredigits(string s) {
    for (int i = 0, n = strlen(s); i < n; i++) {
        if (!(isdigit(s[i]))) {
            return 0;
        }
    }
    return 1;
}

