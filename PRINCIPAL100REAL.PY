import funciones as fn
import statistics
import random

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

sueldos_trabajador = {} 

while True:
    print("---MENU---")
    print("0.- Inicializar Sistema de sueldos")
    print("1.- Asignar sueldos")
    print("2.- Clasificacion de sueldos")
    print("3.- Calcular Estadísticas de sueldos")
    print("4.- Generar planilla de sueldos en csv")
    print("5.- Salir")

    opcion = int(input("Ingrese una opción: "))
    if opcion == 0:
        sueldos_trabajador = {trabajador : 0 for trabajador in trabajadores} 
        print("sueldos inicializados correctamente")
    elif opcion == 1 :
        if not sueldos_trabajador:
            print("Primero debe inicializar los sueldos")
        else:
            sueldos_trabajador = fn.asignar_sueldos(trabajadores)
    elif opcion == 2:
        if sueldos_trabajador :
            fn.clasificar_sueldos(sueldos_trabajador)
        else:
            print("Primero debe asignar sueldos")
    elif opcion == 3:
        if sueldos_trabajador:
            max_sueldo,min_sueldo,promedio_sueldo = fn.calcular_estadisticas(sueldos_trabajador)
            if max_sueldo is not None:
                print("sueldo máximo: $",max_sueldo)
                print("sueldo mínimo: $",min_sueldo)
                print("Promedio de sueldos: $",promedio_sueldo)
            else:
                print("Primero debe asignar sueldos")

    elif opcion == 4:
        if sueldos_trabajador:
            fn.generar_planilla(sueldos_trabajador)
        else:
            print("Primero debe asignar sueldos")

    elif opcion == 5:
        print("Finalizando programa…") 
        print("Desarrollado por Francisco Ortega") 
        print("RUT 18.768.820-5") 
        break
    else:
        print("opcion invalida ingrese una opción entre 0 y 5")

