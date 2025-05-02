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
    noche=int(input())

AI=int
AI2=int
AI3=int
AI4=int

pila=int 
pila=100

while noche==1:
    AI==0
    AI2==3
    AI3==2
    AI4==2
    noche=10

while noche==2:
    AI==0
    AI2==6
    AI3==3
    AI4==3
    noche=20

while noche==3:
    AI==1
    AI2==3
    AI3==7
    AI4==4
    noche=30

while noche==4:
    AI==range(1,20)
    AI2==5
    AI3==6
    AI4==8
    noche=40

while noche==5:
    AI==3
    AI2==8
    AI3==9
    AI4==7
    noche=50

while noche==6:
    AI==4
    AI2==13
    AI3==14
    AI4==18
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

print("12:00AM")
print (" ")

