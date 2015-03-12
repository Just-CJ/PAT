#include<stdio.h>
#include<math.h>
main()
{
	int sum = 0, digit,i, temp, n=0;
	char c;
	c = getchar();
	while(c != '\n'){
		digit = c-'0';
		sum += digit;
		c = getchar();
	}

	temp = sum;
	while(temp){
		digit = temp%10;
		temp /= 10;
		n++;
	}

	for(i = n-1; i > 0; i--){
		digit = sum/((int)pow(10,i));
		sum = sum % ((int)pow(10,i));
		switch(digit){
			case 0:printf("ling");break;
			case 1:printf("yi");break;
			case 2:printf("er");break;
			case 3:printf("san");break;
			case 4:printf("si");break;
			case 5:printf("wu");break;
			case 6:printf("liu");break;
			case 7:printf("qi");break;
			case 8:printf("ba");break;
			case 9:printf("jiu");break;
		}
		printf(" ");
	}

	switch(sum){
			case 0:printf("ling");break;
			case 1:printf("yi");break;
			case 2:printf("er");break;
			case 3:printf("san");break;
			case 4:printf("si");break;
			case 5:printf("wu");break;
			case 6:printf("liu");break;
			case 7:printf("qi");break;
			case 8:printf("ba");break;
			case 9:printf("jiu");break;
		}

	return 0;

}
