from ciudadano import Ciudadano
import random as ran
class Comunidad():
    """docstring for Comunidad."""

    def __init__(self, numero_ciudadano, promedio_conexion, enfermedad,
                  numero_infectados, probabilidad_conexion):
        # atributos
        self.__numero_ciudadano = numero_ciudadano
        self.__lista_ciudadanos = []
        self.__promedio_conexion = promedio_conexion
        self.__enfermedad = enfermedad
        self.__numero_infectados = numero_infectados
        self.__probabilidad_conexion = probabilidad_conexion

        # inicia el ciclo y se generan los ciudadanos
        for i in range(numero_ciudadano):
            self.__lista_ciudadanos.append(Ciudadano(i))

        # aleatorio en la poblacion
        aux = 0
        seleccionado = 0
        while aux < numero_infectados:
            seleccionados = ran.randint(0, numero_infectados)
            if(self.__lista_ciudadanos[seleccionados].infectado == False):
                self.__lista_ciudadanos[seleccionados].infectado = True
                aux = aux + 1

        # setter y getters
    @property
    def numero_ciudadano(self):
        return self.__numero_ciudadano
    @numero_ciudadano.setter
    def numero_ciudadano(self, variable):
        self.__numero_ciudadano = variable

    @property
    def lista_ciudadanos(self):
        return self.__lista_ciudadanos

    @lista_ciudadanos.setter
    def lista_ciudadanos(self, variable):
        self.__lista_ciudadanos = variable
    @property
    def promedio_conexion(self):
        return self.__promedio_conexion

    @promedio_conexion.setter
    def promedio_conexion(self, variable):
        self.__promedio_conexion = variable

    @property
    def dolencia(self):
        return self.__enfermedad

    @dolencia.setter
    def enfermedad(self, variable):
        self.__enfermedad = variable

    @property
    def numero_infectados(self):
        return self.numero_infectados

    @numero_infectados.setter
    def numero_infectados(self, variable):
        self.__numero_infectados = variable

    @property
    def probabilidad_conexion(self):
        return self.__probabilidad_conexion

    @probabilidad_conexion.setter
    def probabilidad_conexion(self, variable):
        self.__probabilidad_conexion = variable
