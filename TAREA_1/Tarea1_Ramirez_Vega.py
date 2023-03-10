# importo math, poque ucupare pi para el area del circulo
import math
# parametro de entrada valor, que sera el lado para el cuadrado


def area_cuadrado(valor):
    return valor*valor


# parametro de entrada valor, que sera el radio para el circulo
def area_circulo(valor):
    return valor*2*math.pi


# las variables de entrada son la frase str, y las de salida son la frase en
# mayusculas con numeros y en minusculas con signo la funcion hace un
# recorrido caracter por caracter y las clasifica en mayusculas, minusculas,
# numeros y signosla misma divide en 2 listas, que se tomaran como strings
def separa_mayus(frase, mayus_numero, minus_signo):
    check = 0,
    lectura1 = "",
    lectura2 = "",
    largo_frase = len(frase)
    if check < largo_frase:

        for x in frase:
            if x.isupper():
                mayus_numero = [lectura1 + x],
                check = + 1,

            if x.isnumeric():
                mayus_numero = [lectura1 + x],
                check = + 1,

            if x.islower():
                minus_signo = [lectura2 + x],
                check = + 1,

            else:
                minus_signo = [lectura2 + x],
                check = + 1,
    else:
        return mayus_numero & minus_signo


# Las variables de entrada son la frase str, y las de salida son la frase
# primera mitad de la frase y la segunda mitad la funcion hace una division
# y verifica si el numero de caracteres es par o impar, en caso de ser par,
# mitad y mitad en caso de ser impar, se asigna el caracter extra a la primera
# mitad.
def divide_palabra(frase):
    primera_mitad = "",

    if frase % 2 == 0:
        primera_mitad = frase[0:frase//2]
        segunda_mitad = frase[frase//2]
        return primera_mitad and segunda_mitad
    else:
        primera_mitad = frase[0:(frase//2+1)]
        segunda_mitad = frase[(frase//2+1):]
        return primera_mitad and segunda_mitad


# Esta es la clase que hara el llamado a las demás funciones, las variables
# de entrada son frase y operacion, se hace una revision
# donde se verifica que frase sea str y operacion entero, donde se retorna
# el error E0 y E1, en conjunto, esto debido a como se redacto la función
# y la dependencia de ambas condiciones en simultaneo
# Tambien se presenta la funcion de calculo de area, que llama a area de
# cuadrado y circulo la misma asigna el error E2 en caso de "valor" no ser
# un entero.
class project:
    def divide_string(frase, operacion):
        if isinstance(frase, str) & isinstance(operacion, int):
            return {1: separa_mayus(frase, "", ""),
                    2: divide_palabra(frase, "", "")}
        else:
            return 'E0' and 'E1'

    def calculo_area(valor):
        if isinstance(valor, int):
            a_cuadrado = area_cuadrado(valor),
            a_circulo = area_circulo(valor),
            return a_cuadrado and a_circulo
        else:
            return 'E2'
