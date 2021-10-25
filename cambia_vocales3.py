def cambia_vocales3():
    palabra= raw_input("PALABRA: ")
    num= raw_input("A QUE LETRA QUIERES QUE LA CAMBIE: ")
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            print(num)
        else:
            if(palabra[cont]=='e'):
                print(num)
            else:
                if(palabra[cont]=='i'):
                    print(num)
                else:
                    if(palabra[cont]=='o'):
                        print(num)
                    else:
                        if(palabra[cont]=='u'):
                            print(num)
                        else:
                            print(palabra[cont])
        cont=cont+1
        
    print("Palabra transformada: "+palabra)

cambia_vocales3()
    
