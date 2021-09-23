def tabla3():
    nombre=raw_input("¿Como te llamas?")
    n=input("¿Que tabla deseas? "+(nombre)+" : ") 
    print("**************************")
    print("*    TABLA DEL "+str(n)+"*")
    print("**************************")
    for cont in range(0,11):
        print(" "+str(n)+" x " +str(cont)+" = "+str(cont*n))
        

tabla3()
    
