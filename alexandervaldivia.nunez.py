import csv
import random
import math
trabajadores = [
    {"nombre": "Juan Perez", "cargo": "consultor ti"},
    {"nombre": "Maria Garcia", "cargo": "analista"},
    {"nombre": "Carlos Lopez", "cargo": "programador"},
    {"nombre": "Ana Martinez", "cargo": "jefe de proyecto"},
    {"nombre": "Pedro Rodriguez", "cargo": "consultor ti"},
    {"nombre": "Laura Hernandez", "cargo": "analista"},
    {"nombre": "Miguel Sanchez", "cargo": "programador"},
    {"nombre": "Isabel Gomez", "cargo": "jefe de proyecto"},
    {"nombre": "Francisco Diaz", "cargo": "consultor ti"},
    {"nombre": "Elena Fernandez", "cargo": "analista"}
]
sueldos = []
def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(len(trabajadores))]
    print("sueldos asignados aleatoriamente")
def clasificar_sueldos():
    print("clasificación de Sueldos")
    menor_800k = []
    entre_800k_2m = []
    mayor_2m = []
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            menor_800k.append(trabajador)
        elif 800000 <= sueldo <= 2000000:
            entre_800k_2m.append(trabajador)
        else:
            mayor_2m.append(trabajador)
    print(f"\nsueldos menores a $800.000: {len(menor_800k)}")
    for emp in menor_800k:
        print(f"nombre: {emp["nombre"]}, cargo: {emp["cargo"]}")
    print(f"\nsueldos entre $800.000 y $2.000.000: {len(entre_800k_2m)}")
    for emp in entre_800k_2m:
        print(f"nombre: {emp["nombre"]}, Cargo: {emp["cargo"]}")
    print(f"\nsueldos mayores a $2.000.000: {len(mayor_2m)}")
    for emp in mayor_2m:
        print(f"nombre: {emp["nombre"]}, cargo: {emp["cargo"]}")
    print(f"\nsueldo total: ${sum(sueldos)}")
def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
    print(f"\nsueldo mas alto: ${sueldo_max}")
    print(f"sueldo mas bajo: ${sueldo_min}")
    print(f"promedio de sueldos: ${sueldo_promedio:.2f}")
    print(f"media geometrica de sueldos: ${sueldo_geom:.2f}")
def reporte_sueldos():
    print("generando reporte de sueldos")
    with open("reporte_sueldos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["nombre empleado", "cargo", "sueldo base", "descuento salud", "descuento AFP", "sueldo liquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([
                trabajador["nombre"], 
                trabajador["cargo"], 
                sueldo, 
                descuento_salud, 
                descuento_afp, 
                sueldo_liquido
            ])
def salir_programa():
    print("generador de sueldos")
    print("desarrollado por [alexander mauel valdivia nunez]")
    print("RUT [21942465-6]")

def menu():
    while True:
        print("\nmenu:")
        print("1. asignar sueldos aleatorios")
        print("2. clasificar sueldos")
        print("3. ver estadisticas")
        print("4. generar reporte de sueldos")
        print("5. salir del programa")
        opcion = int(input("seleccione una opcion: "))
        if opcion == 1:
            asignar_sueldos_aleatorios()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_estadisticas()
        elif opcion == 4:
            reporte_sueldos()
            print("reporte de sueldos generado en reporte_sueldos.csv")
        elif opcion == 5:
            salir_programa()
            break
        else:
            print("opcion no valida ingrese solo las opciones que se le aparece")
if __name__ == "__main__":
    menu()