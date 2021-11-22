def piramide_numerica():
    fil_completa=" "
    num=input("Dame un numero: ")
    for fil in range(num,0,-1):
        for cont in range(1,fil+1):
            fil_completa=fil_completa+str(fil)
        print(fil_completa)
        fil_completa=" "
        

piramide_numerica()
