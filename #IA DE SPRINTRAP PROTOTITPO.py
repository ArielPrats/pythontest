#IA DE SPRINTRAP PROTOTITPO
import random 
 
hola=2
dado=0
mov=0
agresive=0
AI=0
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

AI=int(input( ))

while hola!=1:

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
        print("se a repadado la ventilacion")
        vidavent=10
        rep1=0


    if panel==2:
        print("se esta reparando la camara, espere...")
        rep2=rep2+1

    if rep2==3:
        errorAD=0
        print("se a repadado la camara")
        vidacam=10
        rep2=0


    if panel==3:
        print("se esta reparando el audio, espere...")
        rep3=rep3+1

    if rep3==3:
        errorAD=0
        print("se a repadado el audio")
        vidaaudio=10
        rep3=0


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


    if mov==8 and cam==2:
        print("fase 8/10")

    if mov==8 and cam==1:
        print("8/10 springtrap esta corriendo hacia la puerta")


    if mov==9 and cam==2:
        print("fase 9/10")

    if mov==9 and cam==1:
        print("9/10 springtrap esta asomando por la puerta")


    if mov==10:
        print("fase 10/10")


