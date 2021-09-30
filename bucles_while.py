def bucles_while():
    suma=0
    continuar="S"
    while(continuar=="S"):
        num=input("Introduce un numero: ")
        suma=suma+num
        continuar=raw_input("¿Quieres leer un numero mas?(S/N): ")
    print("SUMA= "+str(suma)) 

bucles_while()
