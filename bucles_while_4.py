def tabla_multiplicar():
    num=input("Dime que tabla quieres ")
    print("TABLA DEL "+str(num))
    cont=0
    while(cont<11):
        print(str(num)) +" x "+ cont+ " = "+num*cont)
        cont=cont+1
        

tabla_multiplicar()
