#include <stdio.h>

int main(void)
{
	int amount = 50;
	float discount;

	printf("Amount: %d\n", amount);
	if (amount >= 100)
	{
		discount = amount * 10 / 100;
		printf("Discount: %f \n", discount);
	}
	else
	{
		printf("Discount not applicable\n");
	}
	return (0);
}
