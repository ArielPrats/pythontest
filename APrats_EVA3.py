#ejercio 1
import os
os.system

mayores=0
menores=0

print("ingrese la cantidad de empleados que desea ingresar")
empleado=int(input())

while empleado!=0:

    try:

        print("ingrese su nombre ")
        nombre=(input())

        print("ingrese años de antiguedad en la empresa")
        años=int(input())

        if años>10:
            mayores=mayores+1
            empleado=empleado-1
        else:
            menores=menores+1
            empleado=empleado-1
    except:
        os.system
        print("porfavor ingrese su nombre y solamente numeros enteros")


print("se registraron", mayores, "empleados con mas de 10 años de antiguedad")
print("se registraron", menores, "empleados con 10 o menos años de antiguedad")

#ejercio2 

entradas=50 
bucle=0
XD=0
si=0
vendidas=0

while bucle!=1:

    print('''
    "CINE FAZ'MOVIE TIME"
    "bienvenido al systema de fazbear ententeirment"
    "que operacion desea realizar?"

    "-.Ver cuantas entradas quedan(1)"

    "-.comprar una cantiad de entradas(2)"

    "-.Salir del faz'movie system(3)
    ''')


    opcion=int(input())

    match opcion:
        case 1:
            print("las entradas dispinibles son de...")
            print(entradas,"dispinibles")
        case 2:
            try:
                print("cuantas entradas desea comprar?")
                venta=int(input( ))
                entradas=entradas-venta
                vendidas=vendidas+venta
            except:
                os.system
                try:
                    print("porfavor solo numeros enteros")
                    print("no pensamos cortar las entradas con tijeras")
                    print("a su medida, gracias...")
                    print("ahora ingrese cuantas entradas desea comprar!")
                    venta=int(input( ))
                    entradas=entradas-venta
                except:
                    os.system
                    print("pero que te eh dicho? solo entradas enteras!")
                    print("gracias!")
        case 3:
            try:
                print("estas seguro que deseas salir del faz'movie system?")
                print("si(1), no(2)")
                si=int(input())

                while si>2:
                    print("error, selecione un comando valido")
                    si=int(input())
                
                if si==1:
                    break
                else:
                    print("puedes proseguir con el sistema")
            except:
                os.system
                print("error, porfavor selecione un comando valido!")
    
    if entradas==0:
        print('''
        "lo siento! se an acabado las entradas"
        ''')
        break

print("as salido del systema de faz'movie system")
print("el total de entradas vendidas es de", vendidas)
print("muchas gracias por usar nuestro sistema!")
print('''

BBBB   \   /  EEEEE     BBBB   \   /  EEEEE   !
B   B   \ /   E         B   B   \ /   E       !
BBBB     Y    EEEE      BBBB     Y    EEEE    !
B   B    Y    E         B   B    Y    E       !
BBBB     Y    EEEEE     BBBB     Y    EEEEE   O
          
''')
