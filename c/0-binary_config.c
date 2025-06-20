#include <stdio.h>
#include <stdlib.h>

typedef unsigned char byte;

int main(int argc, char **argv)
{
	int nb;
	float nbl;
	byte *ptrByte;

	nb = atoi(argv[1]);
	nbl = atof(argv[2]);
	ptrByte = (byte *)&nb;
	printf("\n\n\n\n");
	for (int i = 0; i < (int)sizeof(nb); i++)
	{
		printf("\t\t\t");
		for (int j = 7; j >= 0; j--)
			printf("%d", ptrByte[i] >> j & 1);
		printf("\n");
	}
	printf("\n\n\n\n");
	ptrByte = (byte *)&nbl;
	for (int i = 0; i < (int)sizeof(nbl); i++)
	{
		printf("\t\t\t");
		for (int j = 7; j >= 0; j--)
			printf("%d", ptrByte[i] >> j & 1);
		printf("\n");
	}
	printf("\n\n\n\n");
}
