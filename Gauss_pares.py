def Gauss_pares():
    n=input("Hola buenas, ¿Hasta que numero deseas que cuente? ")
    acum=0
    resto=0
    for cont in range(1,n+1):
        resto=cont % 2
        if(resto==0):
            acum=acum+cont
        print(str(cont) +" acum= "+str(acum))
    
Gauss_pares()

