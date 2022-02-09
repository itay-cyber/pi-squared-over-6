/*
Same program as calc.py, about 4 times faster. 

If you are wanting a better experience, please use this program.

It calculated to 9,999,999,999 numbers which is 9 billion, and the result was 
PI: 3.141592653399594148311280150664970278739929199218750000000000

in about 5 minutes. 




*/

#include <stdio.h>
#include <math.h>

long double total = 0;
long double n = 1;

double get_pi(long double result) 
{
    return sqrt(result * 6);
}
double calc_pi(long double val) 
{
    while (n < val)
    {
        total += 1/(n*n);
        n++;
        if (n < val) 
        {
            calc_pi(n);
        }
        else 
        {
            return total;
        }
    }
}


int main()
{
    printf("PI: %0.60f\n", get_pi(calc_pi(9999999999)));

    return 0;
}


