def devuelve_el_mayor(num1,num2,num3):
    if(num1>num2 and num3):
        mayor=num1
    if(num2>num1 and num3):
        mayor=num2
    if(num3>num1 and num2):
        mayor=num3
    return(mayor)
def preguntas():
    num1=raw_input("Dame un numero: ")
    num2=raw_input("Dame otro numero: ")
    num3=raw_input("Otro numero mas: ")

    print("El numero mayor es: ")+str(devuelve_el_mayor(num1,num2,num3))

preguntas()
        
    
    
