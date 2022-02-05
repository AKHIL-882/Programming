/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int a[10][10],b[10][10];
    int r,c,i,j,evenSum = 0, oddSum = 0;
    scanf("%d %d",&r,&c);
    if(r==c){
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                scanf("%d",&a[i][j]);
            }
        }
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                scanf("%d",&b[i][j]);
            }
        }
    }
    
    int prod[10][10];
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            prod[i][j] = b[i][j] * a[i][j];
        }
    }
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            printf("%d \t",prod[i][j]);
        }
        printf("\n");
    }
}

