import random
import csv
import statistics

def asignar_sueldos(trabajadores):
    
    sueldos_trabajador = {}

    for trabajador in trabajadores:
        
        sueldo = random.randint(300000,2500000)

        sueldos_trabajador[trabajador] = sueldo

    print("sueldos generados aleatoriamente")
    print(sueldos_trabajador)

    return sueldos_trabajador

def clasificar_sueldos(sueldos_trabajador):
    menores_800 = {}
    entre_800_2000000 = {}
    superiores_2000000 = {}

    for trabajador,sueldo in sueldos_trabajador.items():
        if sueldo < 800000:
            menores_800[trabajador] = sueldo
        elif sueldo >= 800000 and 2000000:
            entre_800_2000000[trabajador] = sueldo
        else:
            superiores_2000000[trabajador] = sueldo

    
    print("sueldos menores a $800.000 TOTAL",len(menores_800))
    for trabajador,sueldo in menores_800.items():
        print(trabajador,": $",sueldo)

    print("sueldos entre $800.000 y $2.000.000 TOTAL",len(entre_800_2000000))
    for trabajador,sueldo in entre_800_2000000.items():
        print(trabajador,": $",sueldo)

    print("sueldos mayores a $2.000.000 TOTAL",len(superiores_2000000))
    for trabajador,sueldo in superiores_2000000.items():
        print(trabajador,": $",sueldo)
    
def calcular_estadisticas(sueldos_trabajador):
    
    sueldo = list(sueldos_trabajador.values()) 

    if not sueldo:
        print("No hay sueldos asignados")
        return None,None,None,None
    
    max_sueldo = max(sueldo) 
    min_sueldo = min(sueldo) 
    promedio_sueldos = sum(sueldo) / len(sueldo)
    # media_geometrica = statistics.geometric_mean(sueldo)

    return max_sueldo,min_sueldo,promedio_sueldos,# media_geometrica: me da un error que no supe solucionar
    

    

def generar_planilla(sueldos_trabajador):
    
    with open('planilla_sueldos.csv','w',newline='') as archivo :
        escritor = csv.writer(archivo,delimiter=',')

        
        escritor.writerow(['Nombre empleado','sueldo base','descuento salud','descuento AFP','sueldo liquido'])

        
        for trabajador,sueldo in sueldos_trabajador.items():
            escritor.writerow([trabajador,sueldo])
    print("planilla generada correctamente en planilla_sueldos.csv")
    



