#include <stdio.h>

int main(void)
{
	char ch = '7';

	if (ch >= 48 && ch <= 57)
	{
		printf("The character is a digit.\n");
	}
	else
	{
		printf("The character is not a digit.\n");
	}
	return (0);
}
