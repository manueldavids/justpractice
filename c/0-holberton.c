#include <stdio.h>

int main(void)
{
	int a = 21;
	int b = 10;
	int c;

	printf("a: %d b: %d\n");

if (a == b)
{
	printf("Line 1 - a is equal to b\n");
}
else
{
	printf("Line 1 - a is not equal to b\n");
}

if (a < b)
{
	printf("Line 2 - is a less than b\n");
}
else
{
	printf("Line 2 - a is not less than b\n");
}

if (a > b)
{
	printf("Line 3 - a is greater than b\n");
}
else
{
	printf("Line 3 - a is not grater than b\n");
}
/* Lets change value of a and b */
a = 5;
b = 20;

printf("a: %d b: %d\n", a, b);

if (a <= b)
{
	printf("Line 4 - a is either less than or equal to b\n");
}
if (b >= a)
{
	printf("Line 5 - is either greater than or equal to b\n");
}

if (a != b)
{
	printf("Line 6 - a is not equal to b\n");
}
else
{
	printf("Line 6 - a is equal to b\n");
}

return (0);
}
