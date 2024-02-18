import requests
from datetime import datetime
def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise an exception in case of an error status code
        data = response.json()
        precio_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {'fecha_hora': fecha_hora, 'precio_usd': precio_usd}
    except requests.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return None
def guardar_datos_precio_bitcoin(datos, cantidad_bitcoins, archivo):
    with open(archivo, 'a') as f:
        f.write(f"Fecha y hora: {datos['fecha_hora']}\n")
        f.write(f"Cantidad de bitcoins: {cantidad_bitcoins:.4f}\n")
        f.write(f"Precio de Bitcoin en USD: {datos['precio_usd']:.4f}\n\n")
def main():
    cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    datos_precio_bitcoin = obtener_precio_bitcoin()
    if datos_precio_bitcoin:
        guardar_datos_precio_bitcoin(datos_precio_bitcoin, cantidad_bitcoins, 'precio_bitcoin.txt')
        print("Datos de precio de Bitcoin y cantidad de bitcoins guardados correctamente.")
if __name__ == "__main__":
    main()