##podemos mandar una excepcion con raise
import sys
x = 1

##validamos que el sistema sea windows
def win():
    assert ('linux' in sys.platform),"This code runs on linux only"
    print('Doing something')
##MANDAR UNA EXCEPTION 
#if x > 5:
   # raise Exception('El 11 es mayor al 6 ERROR x ES  = {}' .format(x))

##bloque Try except

try:
    win()

##Exception captura todos los errores
except Exception as error:
    print(error)
    print('no se que paso, pero paso algo mal')
##finally siempre se va ejecutar, recomendacion: Buscar los nombres de los errores para poderlos
##manejar de mejor manera
finally:
    print('se termino el script')
