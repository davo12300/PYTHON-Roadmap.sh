import random

try:
    print('---MAQUINITA GAME---')
    
    gameRun= True
    
    while gameRun == True:

        dinero_maquina= 1000
        coins  = 0 
        opjetos = [ 'CEREZA', 'LIMONES', 'SANDIA', 'ESTRELLAS', 'PILON']
        premio = [ 1 , 2 , 5 , 4 , 10]
        creditos = [0 , 0 , 0 , 0 , 0]
        
        

        while dinero_maquina > 100:
            

            print('----|| CREDITOS : ', coins, '||---')
            for x in range(5):
                print( ' APUESTA --->: $', creditos[x] , '-----' ,opjetos[x] ,'--->PREMIO: $',premio[x] , ' \n --->ELIGIR-----> :', x + 1 )
            
            
                
            
            
                
            choose = int(input('JUGAR = 1 || INGRESAR MONEDAS = 2 \nSELECCIONAR FIGURA = 3 || SALIR = 5 :  '))
            
            credit_count = False
            for f in range (5):
                if creditos[f] > 0 :
                    credit_count = True
            
                
            if choose == 1 and credit_count == True:
                random_game = random.randrange(0 , 5)
                print('-----------PANEL GAME--------------')
                print('HA CAIDO ---->' , opjetos[random_game], '!!<-----')
                print('-----------------------------------')
                if creditos[random_game] > 0:
                    premios = (creditos[random_game] * premio[random_game]) 
                    coins = coins + premios
                    dinero_maquina = dinero_maquina - premios

                    for x in range(5):
                        dinero_maquina = dinero_maquina + creditos[x]

                    print('***************************************')
                    print('VICTORIA!!! , HAS GANADO \t $', premios , 'PESOS')
                    print('*******WINNER***WINNER*** WINNER*******')
                    print('***************************************')
                    creditos = [0 , 0 , 0 , 0, 0]
                else:
                    
                    for x in range(5):
                        dinero_maquina = dinero_maquina + creditos[x]

                    print('---------------------------------')
                    print('PERDISTE :( , VUELVE A INTENTARLO')
                    print('--------LOSER----LOSER----------')
                    print('---------------------------------')
                    creditos = [0 , 0 , 0 , 0 , 0]  
                
            
            
            elif choose == 3 and coins > 0:

                seleccion = int(input('SELECCIONE ALGUNO: '))
                if seleccion == 1:
                    creditos[0] =  creditos[0] + 1
                    coins = coins - 1
                elif seleccion == 2:
                    creditos[1] =  creditos[1] + 1
                    coins = coins - 1
                elif seleccion == 3:
                    creditos[2] =  creditos[2] + 1
                    coins = coins - 1
                elif seleccion == 4:
                    creditos[3] =  creditos[3] + 1
                    coins = coins - 1
                elif seleccion == 5:
                    creditos[4] =  creditos[4] + 1
                    coins = coins - 1
                
                else:
                    print(' ELIGE UNA OPCION VALIDA')
                

            elif choose == 5:
                print('DEVOLVIENDO --- > $' , coins)
                print('FIN DEL JUEGO....')
                gameRun = False

                print('DINERO EN MAQUINA: \t' , dinero_maquina)

                break 
                
            
            else:
            

                money = str(input(' ***  INSERT COIN  \t: '))
                
                coins = coins + int(money)
    
        

except Exception as error:
    print(error)
    print('VERIFICA SI INGRESASTE CADENA DE TEXTO')
    