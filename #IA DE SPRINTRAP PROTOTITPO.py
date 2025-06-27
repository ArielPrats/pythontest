#IA DE SPRINTRAP PROTOTITPO
import random 
 
hola=2
dado=0
mov=0
agresive=0
AI=0
AIPFD=0
AIPFY=0
AIBB=0
vidaaudio=10
vidacam=10
vidavent=10
errorAD=0
errorCAM=0
errorVENT=0
rep1=0
rep2=0
rep3=0
panel=0
ventdoor=0
ataque=0
XD=1

AI=int(input( ))


print("Elija su noche")


print('''
-noche(1)
-noche(2)
-noche(3)
-noche(4)
-noche(5)
-noche(6)
''')

noche=int(input())

while noche>7:
    print("error,no se reconoce noche")
    noche=(input())


pila=int 
pila=100
#FOXY (oh AIPFY, VA POR PORSENTAJE DE "AIPFY<random(1,100)")
while noche==1:
    AI=0
    AIPFD=0
    AIPFY=0
    AIBB=0
    noche=10

while noche==2:
    AI=0
    AIPFD=2
    AIPFY=1
    AIBB=2
    noche=20

while noche==3:
    AI=0
    AIPFD=3
    AIPFY=2
    AIBB=3
    noche=30

while noche==4:
    AI=0
    AIPFD=4
    AIPFY=4
    AIBB=4
    noche=40

while noche==5:
    AI=0
    AIPFD=5
    AIPFY=10
    AIBB=5
    noche=50

while noche==6:
    AI=0
    AIPFD=7
    AIPFY=10
    AIBB=7
    noche=60


while noche==10:
    print("-noche 1")
    print("un nuevo empleo")
    noche=0

while noche==20:
    print("-noche 2")
    print("un nuevo terror")
    noche=0

while noche==30:
    print("-noche 3")
    print("alucinaciones")
    noche=0

while noche==40:
    print("-noche 4")
    print("sigan al conejo amarillo")
    noche=0

while noche==50:
    print("-noche 5")
    print("THE LAST FIGHT!")
    noche=0

while noche==60:
    print("-noche 6")
    print("i hope you die in a fire...")
    noche=0


while hola!=1:

    if XD>=1 and XD<=20:
        print("12:00 AM")
        XD=XD+1

    if XD>=20 and XD<=40:
        print("1:00 AM")
        XD=XD+1

    if XD>=40 and XD<=60:
        print("2:00 AM")
        XD=XD+1

    if XD>=60 and XD<=80:
        print("3:00 AM")
        XD=XD+1

    if XD>=80 and XD<=90:
        print("4:00AM")
        XD=XD+1

    if XD>=90 and XD<=100:
        print("5:00AM")
        XD=XD+1

    if XD==120:
        break


    #IA FUENTE
    num=random.randint(1,20)
    if AI==num or AI>num:
        if errorAD==1:
            dado=random.randint(1,4)
        else:
            dado=random.randint(1,3)

        if dado==2 or dado==3 or dado==4 or agresive==1:
            mov=mov+1
            agresive=0
    else:
        agresive=1


    #SISTEMA DE CAMARAS
    print("quieres ver las camaras, oh el panel de reparacion?")
    print("camaras(1), panel reparacion(2), no habrir(3)")
    cam=int(input())

    if vidacam>1:
        if cam==1:
            cam=1
            print("cam system on")
            vidacam=vidacam-random.randint(1,3)
            #aqui modificar la vida dependiendo de la noche 

        if cam==3:
            cam=3
            print("cam system off")
        
        if cam>3 or cam==0:
            print("error, comando de camara denegado")
            cam=int(input())
    else:
        print("CAMERA ERROR")
        errorCAM=1


    if vidaaudio>1 and cam==1:
        print("quieres usar el audio? si(1), no(2)")
        audio=int(input())

        if audio==1:
            mov=mov-random.randint(1,3)
            print("el audio a sonado")
            vidaaudio=vidaaudio-random.randint(1,3)
            #aqui modificar la vida dependiendo de la noche 

        if audio==2:
            print("audio no usado")
            
        if audio>2 or audio==0:
            print("error, comando de audio denegado")
            audio=int(input())
    elif vidaaudio<1:
        print("ERROR AUDIO") 
        errorAD=1


    if vidavent>1 and cam==1:
        print("cerrar ventilaion? si(1) no(2)")
        vent=int(input( ))

        if vent==1:
            ventdoor=1
            print("se a serrado la ventilacion")
            vidavent=vidavent-random.randint(1,3)
            #aqui modificar la vida dependiendo de la noche 

        if vent==2:
            ventdoor=2
            print("ventilacion abierta")
        
        if vent>2 or vent==0:
            print("error, comando de ventilacion denegado")
            vent=int(input())
    elif vidavent<1:
        print("ERROR VENTILACION") 
        errorVENT=1


    #PANEL REPARACIONES 
    if cam==2:
        print("panel de reparaciones")
        print("-ventilacion(1)",errorVENT)
        print("-camaras(2)",errorCAM)
        print("-audio(3)",errorAD)
        panel=int(input())


    if panel==3:
        print("se esta reparando la ventilacion, espere...")
        rep1=rep1+1

    if rep1==3:
        errorVENT=0
        print("se a reparado la ventilacion")
        vidavent=10
        rep1=0
        panel=0

    if panel==2:
        print("se esta reparando la camara, espere...")
        rep2=rep2+1

    if rep2==3:
        errorCAM=0
        print("se a repadado la camara")
        vidacam=10
        rep2=0
        panel=0


    if panel==3:
        print("se esta reparando el audio, espere...")
        rep3=rep3+1

    if rep3==3:
        errorAD=0
        print("se a repadado el audio")
        vidaaudio=10
        rep3=0
        panel=0


    #SISTEMA DE MOVIMINETO

    if mov==1 and cam==2:
        print("fase 1/10")
        
    if mov==1 and cam==1:
        print("1/10 springtrap despierta")


    if mov==2 and cam==2:
        print("fase 2/10")

    if mov==2 and cam==1:
        print("2/10 springtrap sale de su cueva")


    if mov==3 and cam==2:
        print("fase 3/10")

    if mov==3 and cam==1:
        print("3/10 springrap esta en la arcade")


    if mov==4 and cam==2:
        print("fase 4/10")

    if mov==4  and cam==1:
        print("4/10 springtrap salio de la arcade")


    if mov==5 and cam==2:
        print("fase 5/10")

    if mov==5 and cam==1:
        print("5/10 springtrap esta en el otro pasillo")


    if mov==6 and cam==2:
        print("fase 6/10")
        
    if mov==6 and cam==1:
        print("6/10 springtrap esta en la tienda")


    if mov==7 and cam==2:
        print("fase 7/10")

    if mov==7 and cam==1:
        print("7/10 springtrap esta asomando a la ventana")


    if mov<8 and ataque==2:
        mov=8

    if mov==8 or mov>8:

        ataque=2

        if mov==8 and cam==2:
            print("fase 8/10")

        if mov==8 and cam==1:
            print("8/10 springtrap esta corriendo hacia la puerta")


        if mov==9 and cam==2:
            print("fase 9/10")

        if mov==9 and cam==1:
            print("9/10 springtrap esta detras de la puerta")
        
        if mov==10:
            print("10/10 springtrap esta asomando por la puerta")

    if mov==11:
        print("SPRINGTRAP A ENTRADO A LA OFICINA")
        break


if mov==11:
    print("GAME OVER...")
    print("as sobrevivido",XD)
elif XD==120:
    print("6:00AM! NOCHE COMPLETADA")
    