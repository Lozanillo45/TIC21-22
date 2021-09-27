def Gauss_impares_pares():
    n=input("Hola buenas, ¿Hasta que numero deseas que cuente? ")
    suma_par=0
    suma_impar=0
    suma_total=0
    resto=0
    for cont in range(1,n+1):
        resto=cont % 2
        suma_total=suma_total+cont
        if(resto==0):
            suma_par=suma_par+cont
        else:
            suma_impar=suma_impar+cont
            
        print(str(cont) +" pares= "+str(suma_par)+" impares= "+str(suma_impar))
    print("La suma de los pares= "+str(suma_par))
    print("La suma de los impares= "+str(suma_impar))
    print("La suma TOTAL= "+str(suma_total))
    
Gauss_impares_pares()

