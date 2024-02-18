def contar_lineas_codigo(archivo):
    try:
        if not archivo.endswith('.py'):
            print("El archivo no es un archivo .py válido.")
            return
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            contador = 0
            comentario = False
            for linea in lineas:
                linea = linea.strip()
                if not linea or linea.startswith('#'):
                    continue
                if linea.startswith("'''") or linea.startswith('"""'):
                    comentario = not comentario
                    continue
                if comentario:
                    continue
                contador += 1
            return contador
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
archivo = input("Ingrese la ruta del archivo .py: ")
cantidad_lineas_codigo = contar_lineas_codigo(archivo)
if cantidad_lineas_codigo is not None:
    print(f"El archivo tiene {cantidad_lineas_codigo} líneas de código.")