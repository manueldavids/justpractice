#include <stdio.h>

int main(void)
{
	char op1 = 'F';
	int op2 = 3;

	printf("operand1: %c operand2: %d\n", op1, op2);
	printf("Addition of op1 and op2: %d\n", op1 + op2);
	printf("Subtraction of op2 from op1: %d\n", op1 - op2);
	printf("Multiplication of op1 and op2: %d\n", op1 * op2);
	printf("Division of op1 by op2: %d\n", op1 / op2);

	return (0);
}
