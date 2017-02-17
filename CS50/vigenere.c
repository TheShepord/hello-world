#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int arealpha(string s);
int shift(char c);

int main(int argc, string argv[]) {
    if (argc == 2 && arealpha(argv[1])) {
        string text = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0, n = strlen(text),
             j = 0, lenj = strlen(argv[1]);
             i < n; i++, j++) {

            if (j == lenj) {
               j = 0;
            }

            if (isupper(text[i])) {
                printf("%c",
                       ((text[i]+shift(argv[1][j])-'A')%26)+'A');
            }
            else if (islower(text[i])) {
                printf("%c",
                       ((text[i]+shift(argv[1][j])-'a')%26)+'a');
            }
            else {
                printf("%c",text[i]);
            }
        }
        printf("\n");

    }
    else {
        printf("Usage: ./vigenere keyword");
    }
}

int arealpha(string s) {
    for (int i = 0, n = strlen(s); i < n; i++) {
        if (!(isupper(s[i]) || islower(s[i]))) {
            return 0;
        }
    }
    return 1;
}

int shift(char c) {
    if (isupper(c)) {
        return c - 'A';
    }

    else if (islower(c)) {
        return c - 'a';
    }

    else {
        return 0;
    }
}
