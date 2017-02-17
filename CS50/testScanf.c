#include<stdio.h>
#include<stdlib.h>
int main()
{
    // declaring string
    char x;
    char *str = &x;

    printf("x: ");

    // reading string
    scanf("%s",str);

    // print string
    printf("%s\n",str);

    return 0;
}
