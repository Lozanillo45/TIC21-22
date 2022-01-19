#include<stdio.h>
//ORDENAR UNA LISTA DE NUMEROS POR EL METODO DE LA BURBUJA
int main(){
	int numeros[5];
	int cont;
	int aux;
	int repetir;
	//LEO LA LISTA
	for(cont=0;cont<5;cont++){
		printf("\nDAME UN NUMERO: ");
		scanf("%d",&numeros[cont]);
		
	}
	//LA MUESTRO POR PANTALLA
	printf("\nLISTA DE NUMEROS: ");
		for(cont=0;cont<5;cont++){
			printf("%d ",numeros[cont]);
	}
		
	//LA ORDENO DE MENOR A MAYOR
	for(repetir=1;repetir<5;repetir++){
		for(cont=0;cont<=3;cont++){
		if(numeros[cont]>numeros[cont+1]){
			aux=numeros[cont];
			numeros[cont]=numeros[cont+1];
			numeros[cont+1]=aux;

	}


		}
		}
	//LA VUELVO A MOSTRAR
	printf("\nLISTA ORDENADA: ");
		for(cont=0;cont<5;cont++){
			printf("%d ",numeros[cont]);
}
	
	return(0);
	
	
}
