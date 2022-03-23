package MiCodigo;

public class ManejaFecha {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Fecha fecha1;
		Fecha fecha2;
		fecha1=new Fecha(6,8,2004);
		fecha2=new Fecha(30,6,2004);
		if(fecha1.esPosterior(fecha2)==true) {
			System.out.println("La fecha1 es posterior a la fecha2");
			
			
		}
		else {
			System.out.println("La fecha1 es anterior a la fecha2");
		}
		fecha1.setMes(2);
		System.out.println("El nuevo mes es "+fecha1.getMes(0));
		fecha1.setMes("Enero");
		System.out.println("El nuevo mes es "+fecha1.getMes(1));
	}
	
}
