#include <stdio.h>
#include <stdlib.h>

int get_int_between_1_8(void);
int triangle_right(int height);
int triangle_left(int height);

int main(void)
{
    int height;
    height = get_int_between_1_8();
    triangle_right(height);
    printf("\n");
    triangle_left(height);

    system("pause"); 
    return 0;
}

int triangle_right(int height)
{
    int row;
    for (row = 0; row < height; row++)
    {
        for (int k = 0; k < height - row - 1; k++)
        {
            printf("   ");
        }
        for (int j = 0; j <= row; j++)
        {
            printf(" # ");
        }
        printf("\n"); 
    }
    return 0;
}

int triangle_left(int height)
{
    int row;
    for (row = 0; row < height; row++)
    {
        for (int j = 0; j <= row; j++)
        {
            printf(" # ");
        }
        printf("\n"); 
    }
    return 0;
}

int get_int_between_1_8(void)
{
    int n;
    printf("Height (1-8): ");
    while (scanf("%d", &n) != 1 || n < 1 || n > 8)
    {
        printf("Invalid input. Enter a number between 1 and 8: ");
        while (getchar() != '\n'); // Clear input buffer
    }
    return n;
}
