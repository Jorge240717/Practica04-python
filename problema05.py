def generar_tabla(numero):
    tabla = [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]
    return tabla
def guardar_tabla_en_archivo(tabla, numero):
    nombre_archivo = f"tabla-{numero}.txt"
    with open(nombre_archivo, 'w') as f:
        for linea in tabla:
            f.write(linea + '\n')
def leer_tabla_desde_archivo(numero):
    nombre_archivo = f"tabla-{numero}.txt"
    try:
        with open(nombre_archivo, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("El archivo no existe.")
        return None
def mostrar_tabla(tabla):
    if tabla:
        for linea in tabla:
            print(linea.rstrip()) 
def mostrar_linea_de_tabla(tabla, linea):
    if tabla:
        if linea >= 1 and linea <= len(tabla):
            print(tabla[linea - 1].rstrip())
        else:
            print("El número de línea está fuera de rango.")
def main():
    numero1 = int(input("Ingrese un número entero entre 1 y 10: "))
    if numero1 < 1 or numero1 > 10:
        print("El número debe estar entre 1 y 10.")
        return
    tabla = generar_tabla(numero1)
    guardar_tabla_en_archivo(tabla, numero1)
    print(f"Tabla de multiplicar de {numero1} guardada en el archivo tabla-{numero1}.txt.")
    numero2 = int(input("Ingrese otro número entero entre 1 y 10: "))
    if numero2 < 1 or numero2 > 10:
        print("El número debe estar entre 1 y 10.")
        return
    tabla_leida = leer_tabla_desde_archivo(numero1)
    mostrar_tabla(tabla_leida)
    numero3 = int(input("Ingrese un tercer número entero entre 1 y 10: "))
    if numero3 < 1 or numero3 > 10:
        print("El número debe estar entre 1 y 10.")
        return
    mostrar_linea_de_tabla(tabla_leida, numero3)
if __name__ == "__main__":
    main()