/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int a[10];
    int n,sum=0,i,evenSum = 0, oddSum = 0;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
        if(i%2==0)
            evenSum = evenSum + a[i];
        else
            oddSum = oddSum + a[i];
    }
    printf("%d %d",evenSum,oddSum);
}
