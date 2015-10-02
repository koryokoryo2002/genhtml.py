#include <stdio.h>
#include "sub.h"

void func(int i)
{
	 if(i==0) {
		  printf("if\n");
	 }
}

int main()
{
	 func(6);
	 Sub* sub = new Sub();
	 sub->function(5);
	 return 0;
}
