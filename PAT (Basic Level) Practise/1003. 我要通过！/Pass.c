#include<stdio.h>
main()
{
	int n,i,count1,count2,count3;
	char c;

	scanf("%d", &n);
	c = getchar();
	for(i=0; i<n; i++){
		count1 = 0; count2 = 1; count3 = 0;
		c = getchar();
		while(c != 'P'){
			if(c=='A'){
				c = getchar();
				count1++;}
			else if(c != 'P'){
				printf("NO\n");
				break;
			}
		}

		if(c != 'P'){
			while(c != '\n'){
				c = getchar();
			}
			continue;
		}
		else{
			c = getchar();
			if(c == 'A') c = getchar();
			else{
				printf("NO\n");
				while(c != '\n'){
					c = getchar();
				}
				continue;

			}
		}


		while(c != 'T'){
			if(c == 'A'){
				c = getchar();
				count2++;}
			else if(c != 'T'){
				printf("NO\n");
				break;
			}
		}


		if(c != 'T'){
			while(c != '\n'){
				c = getchar();
			}
			continue;
		}
		else{
			c = getchar();
			while(c != '\n'){
				if(c == 'A'){
					c = getchar();
					count3++;}
				else if(c != '\n'){
					printf("NO\n");
					break;
				}
			}
		}

		if(c != '\n'){
			while(c != '\n'){
				c = getchar();
			}
			continue;
		}else if(count3 == count1*count2) printf("YES\n");
		else printf("NO\n");		
	}

	return 0;
}
