def devuelve_el_mayor_3():
    mayor= input("Introduce un numero: ")
    for cont in range(1,10):
        num=input("Introduce un numero: ")
        if(num>mayor):
            mayor=num
    print("MAYOR= "+str(mayor))

devuelve_el_mayor_3()
        
