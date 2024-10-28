#include <stdio.h>

int main(void)
{
    for (int i = 0; i <= 3; i++)    //should not be <=, should be < only
    {
        printf("#\n");
    }
}