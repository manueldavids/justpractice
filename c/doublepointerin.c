#include <stdio.h>

int main()
{
	int a = 100;

	int *ptr = &a;

	int **dptr = &ptr;

	printf("Value of 'a' is : %d\n", a);
	printf("Value of 'a' using pointer (ptr) is : %d\n, *ptr");
	printf("Value of 'a' using double pointer (dptr) is : %d\n", **dptr);

	return 0;
}
