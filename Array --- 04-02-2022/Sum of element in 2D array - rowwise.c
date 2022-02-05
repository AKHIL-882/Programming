/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int a[10][10];
    int r,c,i,j,evenSum = 0, oddSum = 0;
    scanf("%d %d",&r,&c);
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            scanf("%d",&a[i][j]);
        }
    }
    
    for(i=0;i<r;i++){
        int sum = 0;
        for(j=0;j<c;j++){
            sum = sum + a[i][j];
        }
        printf("%d \t",sum);
    }
}

