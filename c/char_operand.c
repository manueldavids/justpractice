#include <stdio.h>

int main(void)
{

	char a = 'B';
	char b = 'd';


	printf("a: %c b: %c\n", a, b);

if(a == b)
{
	printf("Line 1 - a is equal to b\n");
}
else
{
	printf("Line 1 - a is not equal to b\n");
}

if (a < b)
{
	printf("Line 2 - a is less than b\n");
}
else
{
	printf("Line 2 - is not less than b\n");
}

if (a > b)
{
	printf("Line 3 - a is greater than b\n");
}
else
{
	printf("Line 3 - a is not grater than b\n");
}

if(a != b)
{
	printf("Line 4 - a is not equal to b\n");
}
else
{
	printf("Line 4 - a is equal to b\n");
}

		return(0);
}
