arancel=200000
descuento=0
print('''
    en que comuna vive? 
    1. La florida 20%
    2. La pintana 30%
    3. Puente alto 25%
    4. san Joaquin 15%
    ''')
comuna=int(input("seleccione una comuna: "))

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento=15
else:
    print("seleccion incorrecta")

grupo=int(input("ingrese la cantidad de integrantes de la familia: "))

if grupo==1:
    descuento+=2
elif grupo<=4 and grupo>=2:
    descuento+=3
elif grupo>=5:
    descuento+=4
else:
    print("seleccion incorrecta") 

print("el descuento en total es ", descuento)
desc=arancel*descuento/100
total=arancel-desc
print("el total a pagar es %", total)