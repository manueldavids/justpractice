#include <stdio.h>

int add(int a, int b)
{
	int sum;

	sum = a + b;
	return (sum);
}

int main(void)
{
	int i;
	int j;
	int res;

	i = 2;
	j = 4;
	res = add(i, j);
	printf("%d\n", res);
	return 0;
}
