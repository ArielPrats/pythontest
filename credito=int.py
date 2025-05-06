credito=int
ingresos=int 
educacion=int
nacionalidad=int

print("ingrese su cantidad de ingresos mensuales")

ingresos=int(input( ))

while ingresos>500000 and ingresos<1000000:
    credito=300000
    print("ingrese su nivel de educacion (1)basico, (2)media, (3)superior")
    educacion=int(input( ))
    if educacion==1:
        credito=credito*1
    elif educacion==2:
        credito=credito*1.3
    elif educacion==3:
        credito=credito*1.5

    print("elija su nacionalida (1)Chilena, (2)extranjero ")
    nacionalidad=int(input( ))

    if nacionalidad==1:
        credito=credito+300000
    else:
        credito=credito+0

    break

while ingresos>1000000 and ingresos<1500000:
    credito=650000
    print("ingrese su nivel de educacion (1)basico, (2)media, (3)superior")
    educacion=int(input( ))
    if educacion==1:
        credito=credito*1
    elif educacion==2:
        credito=credito*1.3
    elif educacion==3:
        credito=credito*1.5

    print("elija su nacionalida (1)Chilena, (2)extranjero ")
    nacionalidad=int(input( ))

    if nacionalidad==1:
        credito=credito+300000
    else:
        credito=credito+0

    break

while ingresos>1500000:
    credito=1000000
    print("ingrese su nivel de educacion (1)basico, (2)media, (3)superior")
    educacion=int(input( ))
    if educacion==1:
        credito=credito*1
    elif educacion==2:
        credito=credito*1.3
    elif educacion==3:
        credito=credito*1.5

    print("elija su nacionalida (1)Chilena, (2)extranjero ")
    nacionalidad=int(input( ))

    if nacionalidad==1:
        credito=credito+300000
    else:
        credito=credito+0
    
    break

print("su credito es de...")
print(credito)