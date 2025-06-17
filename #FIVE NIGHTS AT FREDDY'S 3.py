import random
print (''' 
("five nights at freddys 3")
("python Edition")
(" ")
("creado por Ariel Prats")
("fnaf creado por scott cowthon")
(" ")
("ingrese su codigo de empleado:)'
''')

inicio=int(input())

while inicio!=1987: 
    print("error, codigo de fazbear system denegado")
    inicio=int(input())


# lista de cosas por hacer:
#- programar springtrap: IA general y cuartos (10/20 max/ 20/20 agresive mode)
#- programar ventilaciones de IA (si es posible)
#- programar phantoms: freddy, foxy, ballon boy 
#- programar camaras: sistema de audio y ventilacion 
#- programar panel de reparacion: audio, camara, ventilacion 
#- programar errores de systema: y hacer que springtrap se mueva mas rapido 
#- programar modo agresivo (20,20,20,20)
#- programar custom night 

# datos a tomar en cuenta: 
#- noche total 120 turnos 
#- vida de audio antes de error(-1 por uso)(noche1: infinito)(noche2: 5)(noche3: 4)(noche4: 3)(noche5y6: 2) 
#- vida de camara antes de error(-1 por turno)(noche1: infinito)(noche2: 8)(noche3: 7)(noche4: 6)(noche5y6: 4)
#- vida ventilacion antes error(-1 por turno)(noche1: infinito)(noche2: 40)(noche3: 35)(noche4: 30)(noche5: 25)(noche6:random(1,5)per turn)
#- phantoms bajan toda la vida instantaneamente 
#- 
#-

# Niveles de IA:
# phantoms(todos por igual)(noche1: 0)(noche2: 2)(noche3: 3)(noche4: 4)(noche5: 5)(noche6: 7)
# (LA IA DE LOS PHANTOM NO SE ALTERA EN AGRESIVE MOD/solo 2 apariciones por noche)
# P.ballon boy:(ataca en camara)(AIBB/10)(oportunidad cada 7 turnos)(error de audio)
# P.foxy:(% por uso de camara)(ataca en oficina)(noche1: 0%)(noche2: 1%)(noche3: 2%)(noche4: 4%)(noche5: 10%)(noche6: 10%)(error de camara)
# p.freddy:(atacaoficina)(AIF/12)(oportunidad cada 20 turnos)(error de ventilacion)

# SPRINGTRAP:
# ( DADO 1,3 / 1,4 con agresive mod)
# (si DADO es=1 springtrap no se mueve)
# (si dado es mayor a 1 esprintrap se mueve)
# (tengo que investigar su nivel de IA para cada noche)
#