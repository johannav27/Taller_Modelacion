def batallas(B_0, F_0, B_p, F_p, N):
    Barcos_F, Barcos_B = [F_0], [B_0]
    for i in range (N-1):
        Barcos_F.append(Barcos_F[i]-F_p*Barcos_B[i])
        Barcos_B.append(Barcos_B[i]-B_p*Barcos_F[i])

    return Barcos_F, Barcos_B
#Ejercicio 1b
print(batallas(27, 33, .1, .16, 16))


#Ejercicio 1c, abajo
#Total de barcos, abajo británicos=14, francceses=17
#Primera batalla abajo, iniciamos con 9 franceses y 3 británicos
print(batallas(3, 9, .1, .16, 4))
#Terminamos con 8 franceses y .4 britanicos, hemos perdido un frances y 2.6 britanicos

#Segunda batalla abajo, ponemos dos barcos extra en los franceses y se suman 4 britanicos
print(batallas(4.4, 10, .1, .16, 5))
#Terminamos con 8 franceses y 0.7 britanicos, en total hemos perdido 3 franceses y más de 6 británicos

#Tercera batalla
#El resto de los franceses (14) contra el resto de los ingleses (7.3) 
print(batallas(7.3, 14, .1, .16, 7))
#Después de estas tres batallas, terminamos con 10 barcos franceses y 0.2 barcos británicos


#Arriba
#Tenemos en total 16 franceses y 13 británicos 

#Primera batalla, 5 británicos y 10 franceses
print(batallas(5, 10, .1, .16, 6))
#Terminamos con 7.5 franceses y .6 britanicos, hemos perdido 2.5 franceses y 4.4 ingleses

#Segunda batalla, se suman 3 barcos británicos y 2 franceses
print(batallas(3.6, 9.5, .1, .16, 4))
#Terminamos con 8.2 barcos franceses y un barco inglés, en total hemos perdidod 3.8 franceses y 7 ingleses

#última batalla, los que quedan, 
print(batallas(6, 12.2, .1, .16, 6))
#Terminamos con 9 barcos franceses, y 0.7 ingleses

#En total terminamos con 19 barcos franceses y .9 ingleses