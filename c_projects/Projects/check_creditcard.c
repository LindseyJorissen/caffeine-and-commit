#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

long long get_creditcardnumber(void);
bool is_valid_amex(long long credit_card_nr, int num_digits);
bool is_valid_mastercard(long long credit_card_nr, int num_digits);
bool is_valid_visa(long long credit_card_nr, int num_digits);
int get_every_other_digit(long long credit_card_nr);
int get_length_of_number(long long credit_card_nr);

int main(void)
{
    long long credit_card_nr = get_creditcardnumber();
    int sum_every_other_digit = get_every_other_digit(credit_card_nr);
    int num_digits = get_length_of_number(credit_card_nr);
    bool amex = is_valid_amex(credit_card_nr, num_digits);
    bool master = is_valid_mastercard(credit_card_nr, num_digits);
    bool visa = is_valid_visa(credit_card_nr, num_digits);

    if (sum_every_other_digit % 10 != 0)
    {
        printf("INVALID\n");
    }
    else if (amex)
    {
        printf("AMEX\n");
    }
    else if (master)
    {
        printf("MASTERCARD\n");
    }
    else if (visa)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
    
    system("pause"); 
    return 0;
}

long long get_creditcardnumber(void)
{
    long long credit_card_nr;
    printf("Number: ");
    while (scanf("%lld", &credit_card_nr) != 1 || credit_card_nr < 1)
    {
        printf("Invalid input. Enter a valid credit card number: ");
        while (getchar() != '\n'); // Clear input buffer
    }
    return credit_card_nr;
}

bool is_valid_amex(long long credit_card_nr, int num_digits)
{
    int first_two_digits = credit_card_nr / 10000000000000;
    return (num_digits == 15) && (first_two_digits == 34 || first_two_digits == 37);
}

bool is_valid_mastercard(long long credit_card_nr, int num_digits)
{
    int first_two_digits = credit_card_nr / 100000000000000;
    return (num_digits == 16) && (first_two_digits >= 51 && first_two_digits <= 55);
}

bool is_valid_visa(long long credit_card_nr, int num_digits)
{
    int first_digit;
    if (num_digits == 13)
    {
        first_digit = credit_card_nr / 1000000000000;
    }
    else if (num_digits == 16)
    {
        first_digit = credit_card_nr / 1000000000000000;
    }
    else
    {
        return false;
    }
    return first_digit == 4;
}

int get_length_of_number(long long credit_card_nr)
{
    int count = 0;
    while (credit_card_nr > 0)
    {
        count++;
        credit_card_nr /= 10;
    }
    return count;
}

//Luhn’s Algorithm
int get_every_other_digit(long long credit_card_nr)
{
    int sum = 0;
    bool is_second_digit = false;

    while (credit_card_nr > 0)
    {
        int last_digit = credit_card_nr % 10;
        
        if (is_second_digit)
        {
            int doubled = last_digit * 2;
            sum += (doubled / 10) + (doubled % 10);
        }
        else
        {
            sum += last_digit;
        }
        
        is_second_digit = !is_second_digit;
        credit_card_nr /= 10;
    }
    return sum;
}
