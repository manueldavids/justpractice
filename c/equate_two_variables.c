#include <stdio.h>

int main(void)
{
	/* local variable definition */
	int a = 10, b = 0;

	/* while loop execution */
	while(a != b)
{
	a--;
	b++;
		printf("a: %d b: %d\n", a, b);
	}
		printf("\n End of loop");
	return(0);
}
