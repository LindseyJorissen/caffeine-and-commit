#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int guess,tries = 0 ;
    srand(time(0));
    int number = rand() % 100 +1;
    printf("Guess the number game!\n\n");

    do
    {
        printf("Enter a guess between 1 and 100: ");
        scanf("%d",&guess);
        tries++;
        if(guess > number)
        {
            printf("Lower!! \n");    
        }
        else if(guess < number)
        {
            printf("Higher!!! \n");
        }
        else
        {
            printf("Yes! You got it! It took you %i tries! \n",tries);
        }
    } 
    while (guess != number);
    system("pause"); 
    return 0;
}
