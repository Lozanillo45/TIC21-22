#include<stdio.h>

int main(){
	char letra[5];
	int cont;
	
	
	for(cont=0;cont<5;cont++){	
		printf("Introduce la letra %d: ",cont);
		scanf(" %c",&letra[cont]);
	}
	//ESCRIBO datos en la pantalla
	printf("\nHAS ESCRITO LA PALABRA: ");
	for(cont=0;cont<5;cont++){
		printf("%c",letra[cont]);
	
	}
	printf("\n");
	//ESCRIBO LA PALABRA AL REVÉS
	for(cont=4;cont>=0;cont--){
		printf("%c",letra[cont]);
		
	}
	
	return(0);
	
	
}
