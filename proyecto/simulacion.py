import random as ran
from enfermedad import Enfermedad
from ciudadano import Ciudadano
from comunidad import Comunidad

class Simulacion():
    """docstring for Simulacion."""

    def __init__(self, comunidad, enfermedad):
        self.__comunidad = comunidad
        self.__enfermedad = enfermedad

    def simular(self, numero_dias):
        for i in range(numero_dias):
            imprimir_contagiados()
            #contagio_contacto
            pass
    def contagio_contacto(self):

        for i in range(len(self.__comunidad.lista_ciudadanos)):
            prob = ran.randint(0,100)
            if(self.__comunidad.lista_ciudadanos[i].estado and
               self.__comunidad.lista_ciudadanos[i].inmune==False and
               self.__comunidad.lista_ciudadanos[i].sano):
                if prob < (self.__enfermedad.probabilidadInfeccion * self.__comunidad.probabilidad_conexion*100):
                    self.__comunidad.lista_ciudadanos[i].sano = False
                    self.__comunidad.lista_ciudadanos[i].infectado = True
        pass

    def imprimir_contagiados(self):
        contador_contagio = 0
        contador_total = 0
        for i in range(len(self.__comunidad.lista_ciudadanos)):
            if(self.__comunidad.lista_ciudadanos[i].infectado):
                contador_contagio = contador_contagio + 1
            if(self.__comunidad.lista_ciudadanos[i].estado):
                contador_total = contador_total + 1
        print("La cantidad de contagiado es de {0}".format(contador_contagio))
        print("y la cantidad de personas vivas que hay son ", contador_total)
