from enfermedad import Enfermedad
from ciudadano import Ciudadano
from comunidad import Comunidad
from simulacion import Simulacion
def main():

    # enfemerdad con pruebas
    virus_Z = Enfermedad(probabilidadInfeccion=0.3, promedio_pasos=18)
    #print(enfermedad.promedioPasos)
    #enfermedad.promedioPasos = 5
    #print(enfermedad.promedioPasos)

    #ciudadano con pruebas
    #ciudadano = Ciudadano(ID=1)
    #print(ciudadano.infectado)
    #ciudadano.infectado = True
    #print(ciudadano.infectado)
    comunidad = Comunidad(numero_ciudadano=1000,promedio_conexion=8,
                          enfermedad=virus_Z,numero_infectados=10,
                           probabilidad_conexion=0.9)

    simulador = Simulacion(comunidad, virus_Z)
    simulador.imprimir_contagiados()
    simulador.contagio_contacto()
    simulador.imprimir_contagiados()


if __name__ == "__main__":
    main()
