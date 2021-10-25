def analizador_palabras ():
    palabra=raw_input("Dime una palabra ")
    letras=0
    vocales=0
    consonantes=0
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]in"aeiou"):
            vocales=vocales+1
        else:
            consonantes=consonantes+1
        cont=cont+1
        letras=letras+1
    print("Vocales= "+str(vocales))
    print("Consonantes= "+str(consonantes))
    print("Letras= "+str(letras))

    
analizador_palabras()
