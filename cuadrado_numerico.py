#11111
#10001
#10001
#10001
#11111
def cuadrado_numerico():
    linea=" "
    num=input("Dame un numero: ")
    for fil in range(1,num+1):
        if(fil%2==1):
            letra="1"
        else:
            letra="0"
        linea=" "
        for col in range(1,num+1):
            linea=linea+str(letra)
        print(linea)
    linea=" "
    
        
        

cuadrado_numerico()
        
    
