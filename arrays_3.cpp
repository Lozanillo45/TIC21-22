#include<stdio.h>

int main(){
	float x[10];
	int cont;
	float suma=0;
	float media;
	//for cont in range(1,10):
	//cont++ equivale a cont=cont+1
	for(cont=0;cont<10;cont++){
		//num=input("dame un numero: )	
		printf("Dame un numero: ");
		scanf("%f",&x[cont]);
	}
	//ESCRIBO datos en la pantalla
	for(cont=0;cont<10;cont++){
		printf("\n%.2f",x[cont]);
		suma+=x[cont];
		//suma=suma+x[cont]
	}
	media=suma/cont;
	printf("\nLA MEDIA VALE= %.2f",media);
	
	return(0);
	
	
}
