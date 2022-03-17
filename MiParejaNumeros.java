package MiCodigo;

public class MiParejaNumeros {
	//Aquí van los atributos
	int num1;
	int num2;
	//El constructor
	public MiParejaNumeros(int num1, int num2){
		this.num1=num1;
		this.num2=num2;
		
		
	}
	public int getNum1() {
		return num1;
	}
	public int getNum2() {
		return num2;
	}
	
	//Resto de métodos
	public int devuelveSuma(){
		return(num1+num2);
		
	}
	public int devuelveResta(){
		return(num1-num2);
		
		
	}
	public int devuelveMultiplicacion() {
		return(num1*num2);
	}
	public float devuelveDivision() {
		float division;
		division=num1/num2;
		return(division);
		
	}
}
