package MiCodigo;

public class CocheElectrico extends Coche{
	private double potencia;
	public CocheElectrico(String identificador, String medio) {
		super(identificador, medio);
		// TODO Auto-generated constructor stub
	}
	public double getPotencia() {
		return potencia;
	}
	public void setPotencia(double potencia) {
		this.potencia = potencia;
	}

}
