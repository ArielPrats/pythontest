import random
print (''' 
("five nights at freddys")
("python Edition")
("vercion 0.1")
(" ")
("creado por Ariel Prats")
("fnaf creafo por scott cowthon")
(" ")
("ingrese su codigo de empleado:)'
''')

inicio=int(input())

while inicio!=1987: 
    print("error, codigo de fazbear system denegado")
    inicio=int(input())

print("Elija su noche")


print('''
-noche(1)
-noche(2)
-noche(3)
-noche(4)
-noche(5)
-noche(6)
-custom Night(7)
''')

noche=int(input())

while noche>7:
    print("error,no se reconoce noche")
    noche=(input())


pila=int 
pila=100

while noche==1:
    AI=0
    AI2=3
    AI3=2
    AI4=2
    noche=10

while noche==2:
    AI=0
    AI2=6
    AI3=3
    AI4=3
    noche=20

while noche==3:
    AI=1
    AI2=3
    AI3=7
    AI4=4
    noche=30

while noche==4:
    AI=random.randint(1,20)
    AI2=5
    AI3=6
    AI4=8
    noche=40

while noche==5:
    AI=3
    AI2=8
    AI3=9
    AI4=7
    noche=50

while noche==6:
    AI=4
    AI2=13
    AI3=14
    AI4=18
    noche=60

while noche==7:
    print("noche personalizada")
    print(" ")
    
    print("elija el nivel de IA del 1 al 20 para FREDDY")
    AI=int(input())

    while AI>20:
        print("error, elija un numero del 1 al 20")
        AI=int(input())
        
    print("elija el nivel de IA del 1 al 20 para BONNIE")
    AI2=int(input())

    while AI2>20:
        print("error, elija un numero del 1 al 20")
        AI2=int(input())
   
    print("elija el nivel de IA del 1 al 20 para CHICA")
    AI3=int(input())

    while AI3>20:
        print("error, elija un numero del 1 al 20")
        AI3=int(input())

    print("elija el nivel de IA del 1 al 20 para FOXY")
    AI4=int(input())

    while AI4>20:
        print("error, elija un numero del 1 al 20")
        AI4=int(input())
 
    noche=70

print(" ")


while noche==10:
    print("-noche 1")
    print("un nuevo empleo")
    noche=0

while noche==20:
    print("-noche 2")
    print("parecen molesstos")
    pila=pila-9
    noche=0

while noche==30:
    print("-noche 3")
    print("que buscan de mi?")
    pila=pila-11
    noche=0

while noche==40:
    print("-noche 4")
    print("porque te quiedes quedar?")
    pila=pila-13
    noche=0

while noche==50:
    print("-noche 5")
    print("te deseamos suerte")
    pila=pila-18
    noche=0

while noche==60:
    print("-noche 6")
    print("una... ultima... noche")
    pila=pila-20
    noche=0

while noche==70:
    print("CUSTOM NIGHT")
    print("personaliza tu tortura")
    print("elije tu porsentaje de bateria")
    pila=int(input())
    noche=0



XD=1
mov1=0
mov2=0
mov3=0
mov4=0
num=0
spawn=1


while XD!=90 or mov1!=17 or mov2!=15 or mov3!=13 or mov4!=11:
    
    if XD>=1 and XD<=15:
        print("12:00 AM")
        XD=XD+1

    if XD>=15 and XD<=30:
        print("1:00 AM")
        XD=XD+1

    if XD>=30 and XD<=45:
        print("2:00 AM")
        XD=XD+1

    if XD>=45 and XD<=60:
        print("3:00 AM")
        XD=XD+1

    if XD>=60 and XD<=75:
        print("4:00AM")
        XD=XD+1

    if XD>=75 and XD<=90:
        print("5:00AM")
        XD=XD+1

    if XD==90:
        break


    cam=int

    if pila<1:
        print("se te acabo la bateria")
        print("FREDDY: HOG HOG HOG HOG HOG")
        mov1=17
    else:
        print("bateria ",pila,"%")


    print("quieres ver las camaras? si(1) o no(2)")
    cam=int(input())

    if cam==1:
        cam=1
        pila=pila-1
        print("cam system on")
    
    if cam==2:
        cam=2
        print("cam system off")
     
    if cam>2 or cam==0:
        print("error, comando de camara denegado")
        cam=int(input())

  

    num=random.randint(1,20)

    if AI==num or AI>num:
        mov1=mov1+1
    else:
        print("-FREDDY")

    if mov1==1 and cam==2:
        print("-FREDDY")
        mov1=mov1+1

    if mov1==1 and cam==1:
        print("-FREDDY esta en el esenario")
        mov1=mov1+1

    if mov1==3 and cam==2:
        print("-FREDDY")
        mov1=mov1+1

    if mov1==3 and cam==1:
        print("-FREDDY esta en el comedor")
        mov1=mov1+1

    if mov1==5 and cam==2:
        print("-FREDDY")
        mov1=mov1+1

    if mov1==5 and cam==1:
        print("-FREDDY esta en el baño")
        mov1=mov1+1    

    if mov1==7 and cam==2:
        print("-FREDDY")
        mov1=mov1+1

    if mov1==7 and cam==1:
        print("-FREDDY esta llendo a la cosina")
        mov1=mov1+1    

    if mov1==9 and cam==2:
        print("-FREDDY")
        mov1=mov1+1

    if mov1==9 and cam==1:
        print("-FREDDY esta en la cosina")
        mov1=mov1+1    

    if mov1==11 and cam==2:
        print("-FREDDY")
        mov1=mov1+1

    if mov1==11 and cam==1:
        print("-FREDDY esta llendo al pasillo derecho")
        mov1=mov1+1    

    if mov1==13 and cam==2:
        print("-FREDDY")
        mov1=mov1+1

    if mov1==13 and cam==1:
        print("-FREDDY esta en pasillo derecho")
        mov1=mov1+1    

    if mov1==15 and cam==2:
        print("-FREDDY")
        mov1=mov1+1

    if mov1==15 and cam==1:
        print("-FREDDY esta en la puerta derecha")
        mov1=mov1+1    


    num2=random.randint(1,20)

    if AI2==num2 or AI2>num2:
        mov2=mov2+1
    else:
        print("-BONNIE")

    if mov2==1 and cam==2:
        print("-BONNIE")
        mov2=mov2+1

    if mov2==1 and cam==1:
        print("BONNIE esta en el esenario")
        mov2=mov2+1

    if mov2==3 and cam==2:
        print("-BONNIE")
        mov2=mov2+1

    if mov2==3 and cam==1:
        print("BONNIE esta en el comedor")
        mov2=mov2+1

    if mov2==5 and cam==2:
        print("-BONNIE")
        mov2=mov2+1

    if mov2==5 and cam==1:
        print("BONNIE esta en partes y servicios")
        mov2=mov2+1

    if mov2==7 and cam==2:
        print("-BONNIE")
        mov2=mov2+1

    if mov2==7 and cam==1:
        print("BONNIE esta llendo al pasillo izquierdo")
        mov2=mov2+1
    
    if mov2==9 and cam==2:
        print("-BONNIE")
        mov2=mov2+1

    if mov2==9 and cam==1:
        print("BONNIE esta en el pasillo izquierdo")
        mov2=mov2+1

    if mov2==11 and cam==2:
        print("-BONNIE")
        mov2=mov2+1

    if mov2==11 and cam==1:
        print("BONNIE esta en el closed de aseo")
        mov2=mov2+1

    if mov2==13 and cam==2:
        print("-BONNIE")
        mov2=mov2+1

    if mov2==13 and cam==1:
        print("BONNIE esta en la puerta izquierda")
        mov2=mov2+1

   
    num3=random.randint(1,20)

    if AI3==num3 or AI3>num3:
        mov3=mov3+1
    else:
        print("-CHICA")

    if mov3==1 and cam==2:
        print("-CHICA")
        mov3=mov3+1

    if mov3==1 and cam==1:
        print("CHICA esta en el esenario")
        mov3=mov3+1

    if mov3==3 and cam==2:
        print("-CHICA")
        mov3=mov3+1

    if mov3==3 and cam==1:
        print("CHICA esta en el comedor")
        mov3=mov3+1

    if mov3==5 and cam==2:
        print("-CHICA")
        mov3=mov3+1

    if mov3==5 and cam==1:
        print("CHICA esta en la cocina")
        mov3=mov3+1

    if mov3==7 and cam==2:
        print("-CHICA")
        mov3=mov3+1

    if mov3==7 and cam==1:
        print("CHICA esta caminando al pasillo derecho")
        mov3=mov3+1

    if mov3==9 and cam==2:
        print("-CHICA")
        mov3=mov3+1

    if mov3==9 and cam==1:
        print("CHICA esta en el pasillo derecho")
        mov3=mov3+1

    if mov3==11 and cam==2:
        print("-CHICA")
        mov3=mov3+1

    if mov3==11 and cam==1:
        print("CHICA esta en la puerta derecha")
        mov3=mov3+1

    #arreglar a foxy: cuando ves las camaras no aparece devido al tema de numeros pares en su "mov"

    num4=random.randint(1,20) 

    if spawn==1:
        print("-FOXY")
        spawn=spawn+2

    if cam==1:

        if mov4==1 or mov4==2:
            print("FOXY esta en la pirate cover")

        if mov4==3 or mov4==4:
            print("FOXY esta asomando por la cortina")

        if mov4==5 or mov4==6:
            print("FOXY esta saliendo de su cueva")

        if mov4==7 or mov4==8:
            print("FOXY esta asomando en el pasillo izquierdo")

        if mov4==9:
            print("FOXY esta corriendo a la oficina")
            mov4=mov4+1
    
    if cam==2:

        if AI4==num4 or AI4>num4:
            mov4=mov4+1
        else:
            print("-FOXY")

        if mov4==1:
            print("-FOXY")
            mov4=mov4+1

        if mov4==3:
            print("-FOXY")
            mov4=mov4+1        

        if mov4==5:
            print("-FOXY")
            mov4=mov4+1

        if mov4==7:
            print("-FOXY")
            mov4=mov4+1

        if mov4==9:
            print("-FOXY")
            mov4=mov4+1



    print("cerrar puerta izquierda(1), puerta derecha(2)")
    print("cerrar ambas(3), no cerrar ninguna(4)")
    puerta=int(input())

    if puerta==1:
        puerta=1
        pila=pila-1
        print("puerta izquierda cerrada")

    if puerta==2:
        puerta=2
        pila=pila-1
        print("puerta derecha cerrada")
    
    if puerta==3:
        puerta=3
        pila=pila-2
        print("ambas puertas cerradas")

    if puerta==4:
        puerta=4
        print("puertas abiertas")

     
    if puerta>4 or puerta<1:
        print("error, comando de puerta denegado")
        puerta=int(input())


    if mov1==16 and puerta==2 or mov1==16 and puerta==3:
        mov1=1
        print("-FREDDY vuelve al esenario")

    if mov1==16 and puerta==1 or mov1==16 and puerta==4:
        print("FREDDY a entrado a la oficina")
        mov1=17
        break
    

    if mov2==14 and puerta==1 or mov2==14 and puerta==3:
        mov2=1
        print("-BONNIE vuelve al esenario")

    if mov2==14 and puerta==2 or mov2==14 and puerta==4:
        print("BONNIE a entrado a la oficina")
        mov2=15
        break
    

    if mov3==12 and puerta==2 or mov3==12 and puerta==3:
        mov3=1
        print("-CHICA vuelve al esenario")

    if mov3==12 and puerta==1 or mov3==12 and puerta==4:
        print("CHICA a entrado a la oficina")
        mov3=13
        break
    

    if mov4==10 and puerta==1 or mov4==10 and puerta==3:
        mov4=1
        pila=pila-5
        print("-FOXY vuelve al pirate cover")

    if mov4==10 and puerta==2 or mov4==10 and puerta==4:
        print("FOXY a entrado a la oficina")
        mov4=11
        break
    

    golden=0
    golden2=0
    mov=0

    golden=random.randint(1,50000)
    golden2=random.randint(1,50000)

    if golden==golden2:
        print('''
            "          0 0 0 0 0 0          "
			"          0         0          "
			"0 0 0     0=========0     0 0 0"
			"0   0   0 0 0 0 0 0 0 0   0   0"
			"0 0 0 0                 0 0 0 0" 
			"    0   0 0 0     0 0 0   0    " 
			"    0   0 o 0     0 o 0   0    "
			"    0   0 0_       _0 0   0    " 
		    "    0       0 0 0 0       0    "
			"  0     0 0         0 0     0  "
			"  0   0     0 0 0 0     0   0  "
			"  0   0                 0   0  "
			"    0   0 0 0 0 0 0 0 0   0    " 
			"    0 =================== 0    " 
			"    0 =================== 0    " 
			"      0 0 0 0 0 0 0 0 0 0      " 
            ''')
        golden=2
        golden2=1
        mov=9
        break


if XD==90:
    print("6:00AM, Noche Completada!")
    print(" ")
else:
    print("GAME OVER")
    print("turnos sobrevividos")
    print(XD)