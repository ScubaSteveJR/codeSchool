#include <stdbool.h>
#include <stdio.h>

int main(void)
{
    int i = 3;
    while (i > 0)
    {
        printf("meow\n");
        i--;
    }

    while (i < 3)
    {
        printf("meow\n");
        i++;
    }

    for (int i = 0; i < 3; i++)
    {
        printf("meow\n");
    }

    while (true)
    {
        printf("meow\n");
    }
}