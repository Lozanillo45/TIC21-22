package MiCodigo;

public class Circunferencia {
	//ATRIBUTOS
	
	private MiParejaNumeros centroCirculo;
	private double radio;
	public Circunferencia(int coordX, int coordY, double radio) {
		super();
		centroCirculo=new MiParejaNumeros(coordX,coordY);
		this.radio = radio;
		
	}
	public int getCoordX(int coordX) {
		return (centroCirculo.getNum1(coordX));
	}
	public void setCoordX(int coordX) {
		centroCirculo.getNum2();
	}
	public int getCoordY() {
		return coordY;
	}
	public void setCoordY(int coordY) {
		this.coordY = coordY;
	}
	public double getRadio() {
		return radio;
	}
	public void setRadio(double radio) {
		this.radio = radio;
	}
	public double getArea() {
		double area;
		area=Math.PI*Math.pow(radio, 2);
		return area;
	}
	public double devuelveLongitud(){
		double longitud;
		longitud=2*Math.PI*radio;
		return longitud;
	}
		
	}
	
		
	


