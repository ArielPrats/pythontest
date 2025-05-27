tarjeta=1000000
deuda=100000
precio=0
math=0
roll1=0
roll2=0
roll3=0
roll4=0
hola=0

bucle=1

while bucle==1:

    print("bienbenido, porfavor elija su tipo de transaccion")
    print("su saldo actual es de:", tarjeta)
    print("1.- Pagar deuda")
    print("2.- realizar compra de producto")
    print("3.- salir del programa")


    eleccion=int(input( ))


    match eleccion:
        case 1:
            while eleccion==1:
                print("ingrese el monto que desea pagar")

                monto=int(input( ))

                if monto>0 or monto==0:
                    deuda=deuda-monto
                    tarjeta=tarjeta-monto
                    print("su deuda restante a pagar es de", deuda)
                    print("su saldo total es de", tarjeta)
                    break
                elif monto<0:
                    print("error, dijito no apto")
                    monto=int(input( ))
        case 2:
            while hola==0:

                print("bienbenido, porfavor selecione su pedido")
                print("pikachu roll $4500 (1)")
                print("Otaku roll $5000 (2)")
                print("pulpo venenoso roll $5200 (3)")
                print("anguila electrica roll $4800 (4)")
                print("salir a pagar (5)")
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
                        print("pikachu rolls", roll1 )
                        print("otaku rolls", roll2 )
                        print("pulpo venenoso rolls", roll3 )
                        print("anguilaelectrica rolls", roll4 )
                        print("El total a pagar es de", precio)
                        print("desea pagar (1) oh cancelar la transaccion (2)")

                        pagar=int(input( ))

                        while pagar>=3: 
                            print("error, codigo no encontrado")
                            pagar=int(input())

                        if pagar==1:
                            tarjeta=tarjeta-precio
                            print("pedido pagado su saldo restante es de", tarjeta)
                            break
                        elif pagar==2:
                            print("saliendo del programa")
                            break
        case 3:
            print("saliendo del programa")
            break

print("transaccion terminada su saldo total es de")
print(tarjeta)