#include <stdio.h>

int main(void)
{
	/* local variable definition */
	char choice = 'a';

	int x = 0;

	/* while loop execution */
	while(x >= 0)
{
	(x % 2 == 0) ? printf("%d is Even\n", x) : printf("%d is Odd\n", x);
	
	printf("\n Enter a positive number: ");
	scanf("%d", &x);
	}
	printf("\n End of loop");
	return(0);
}
