def cuadrado_numerico2():
    linea=" "
    num=input("Dame un numero: ")
    for fil in range(1,num+1):
        if(fil==1 and num):
            letra="1"
        else:
            letra="0"
        linea=" "
        for col in range(1,num+1):
            if(col==1 and num):
                letra="1"
            else:
                letra="0"
            linea=linea+str(letra)
        print(linea)
    linea=" "
    
        
        

cuadrado_numerico2()
