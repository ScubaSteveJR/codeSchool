#include <stdio.h>

void print_grid(int size);
int get_size(void);

int main(void)
{
    int n = 9;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }

    int h;
    do
    {
        h = get_int("Size: ");
    } while (h < 1);
    

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < h; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

int get_size(void)
{
    int n;
    do
    {
        n = get_int("Size: ");
    } while (n < 1);
    return n;
    
}

void print_grid(int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}