def cambia_vocales4():
    palabra= raw_input("PALABRA: ")
    num= raw_input("A QUE LETRA QUIERES QUE LA CAMBIE: ")
    nueva_palabra=" "
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=='a'):
            nueva_palabra=nueva_palabra+(num)
        else:
            if(palabra[cont]=='e'):
                nueva_palabra=nueva_palabra+(num)
            else:
                if(palabra[cont]=='i'):
                    nueva_palabra=nueva_palabra+(num)
                else:
                    if(palabra[cont]=='o'):
                        nueva_palabra=nueva_palabra+(num)
                    else:
                        if(palabra[cont]=='u'):
                            nueva_palabra=nueva_palabra+(num)
                        else:
                            nueva_palabra=nueva_palabra+(palabra[cont])
        cont=cont+1
        
    print("Palabra transformada: "+palabra)

cambia_vocales4()
    
