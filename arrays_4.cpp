#include<stdio.h>

int main(){
	char letra[10];
	int cont;
	
	
	for(cont=0;cont<10;cont++){	
		printf("Introduce la letra %d: ",cont);
		scanf(" %c",&letra[cont]);
	}
	//ESCRIBO datos en la pantalla
	printf("\nHAS ESCRITO LA PALABRA: ");
	for(cont=0;cont<10;cont++){
		printf("%c",letra[cont]);
	
	}
	
	
	return(0);
	
	
}
