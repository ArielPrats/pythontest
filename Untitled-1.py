

bucle=0
precio=0
math=0
roll1=0
roll2=0
roll3=0
roll4=0
hola=0
compra=0

while hola==0: 

    while bucle!=1:

        print("bienbenido, porfavor selecione su pedido")
        print("pikachu roll $4500 (1)")
        print("Otaku roll $5000 (2)")
        print("pulpo venenoso roll $5200 (3)")
        print("anguila electrica roll $4800 (4)")
        print("salir y pagar (5)")
        print(" ")
        pedido=int(input( ))

        while pedido>6 or pedido==0: 
            print("error, codigo no encontrado")
            pedido=int(input())

        print("")

        match pedido:
            case 1:
                precio=precio+4500
                math=math+4500
                print("su pedido es de:",precio)
                roll1=roll1+1
            case 2:
                precio=precio+5000
                math=math+5000
                print("su pedido es de:",precio)
                roll2=roll2+1
            case 3:
                precio=precio+5200
                math=math+5200
                print("su pedido es de:",precio) 
                roll3=roll3+1          
            case 4:
                precio=precio+4800
                math=math+4800
                print("su pedido es de:",precio)
                roll4=roll4+1
            case 5:
                print("saliendo del programa")
                bucle=1
        
        print(" ")

    print("pikachu rolls", roll1 )
    print("otaku rolls", roll2 )
    print("pulpo venenoso rolls", roll3 )
    print("anguilaelectrica rolls", roll4 )
    print("tiene codigo de descuento?")
    print("poner codigo (1), pagar directamente (2)")
    codigo=int(input( ))

    HD=1

    while codigo==1:

        if codigo==1 and HD==1:
            print("ingrese su codigo")
            codigo1=input( )
            HD=2
            
        if codigo1=="soyutaku":
            math=math/10
            precio=precio-math
            print("su precio a pagar es",precio)
            break

        if codigo1!="soyutaku": 
            print("error, codigo no encontrado")
            codigo1=input( )

    while codigo==2:
        if codigo==2:
            print("su precio a pagar es de", precio)
            break

    print("desea hacer otra compra? si(1), no(2)")

    compra=int(input( ))

    if compra==1:
        hola=0
    elif compra==2:
        break

print("cerrando programa")


