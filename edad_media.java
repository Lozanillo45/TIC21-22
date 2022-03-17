import javax.swing.JOptionPane;

public class edad_media {
	public static vold main(string[]args) {
		int edad, sumaEdad=0, conteoMayor18=0, contadorMayor175=0;
		float altura,sumaAltura=0;
		
		for(int i=1; i<=5; i++) {
			edad= Integer.parseInt(JOptionPane.showInputDialog("Alumno"+i+"\nDigite su edad: "));
			altura = Float.parseFloat(JOptionPane.showInputDialog("Alumno"+i+"\nDigite su altura:")),
			
			sumaEdad +=edad;  // Suma iterativa de edades
			SumaAltura += altura; //Suma iterativa de las alturas
			
			if(edad > 18) { //Si la latura es mayor a 18
				conteoMayor175++;
			}
			if (altura>1.75) {// Si la altura es mayor a 1.75
				contadorMayor1.75++,
			}
		}
		mediaEdad= (float) sumaEdad/30;
		mediaAltura= (float) sumaAltura/30;
		
		System.out.println("La edad promedio es: "+mediaEdad);
		System.out.println("La estatura media es: "+mediaAltura);
		System.out.println("Cantidad de alumnos mayores a 18 años"+conteoMayor18);
		System.out.println("Cantidad de alumnos que miden mas de 1.75"+contadorMayor);
	}
}

