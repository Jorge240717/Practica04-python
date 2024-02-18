import requests
import sqlite3

def obtener_tipo_cambio_anual(year):
    tipo_cambio_anual = []
    # Hacer una solicitud para cada mes del año
    for month in range(1, 13):
        try:
            url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={month}&year={year}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # Filtrar los datos de tipo de cambio de ese mes
                for dato in data:
                    tipo_cambio_mes = {
                        "fecha": dato["fecha"],
                        "compra": dato["compra"],
                        "venta": dato["venta"]
                    }
                    # Agregar los datos de tipo de cambio de ese mes a la lista
                    tipo_cambio_anual.append(tipo_cambio_mes)
            else:
                print(f"Error al obtener los datos del mes {month}. Código de estado: {response.status_code}")
        except Exception as e:
            print(f"Error al obtener los datos del mes {month}: {e}")
    return tipo_cambio_anual

def guardar_en_base_de_datos(tipo_cambio):
    # Conectar a la base de datos o crearla si no existe
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info
                      (fecha TEXT, compra REAL, venta REAL)''')

    # Insertar los datos en la tabla
    for dato in tipo_cambio:
        cursor.execute("INSERT INTO sunat_info VALUES (?, ?, ?)", (dato["fecha"], dato["compra"], dato["venta"]))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def mostrar_tabla():
    # Conectar a la base de datos
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Obtener todos los datos de la tabla
    cursor.execute("SELECT * FROM sunat_info")
    filas = cursor.fetchall()

    # Mostrar los datos
    print("Contenido de la tabla sunat_info:")
    for fila in filas:
        print(fila)

    # Cerrar la conexión
    conn.close()

# Obtener el tipo de cambio de todos los meses del año 2023
tipo_cambio_2023 = obtener_tipo_cambio_anual(2023)

# Guardar los datos en la base de datos
if tipo_cambio_2023:
    guardar_en_base_de_datos(tipo_cambio_2023)
    print("Datos guardados correctamente en la base de datos.")
    # Mostrar el contenido de la tabla
    mostrar_tabla()
else:
    print("No se pudieron obtener datos para el año 2023.")





