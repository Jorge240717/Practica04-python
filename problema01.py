import requests
def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))  
    except requests.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return None
def calcular_costo_bitcoins(bitcoins, precio_bitcoin):
    if precio_bitcoin is None:
        return None
    return bitcoins * precio_bitcoin
def main():
    n = input("Ingrese la cantidad de bitcoins que posee: ")
    try:
        n = float(n)
    except ValueError:
        print("Ingrese un número válido.")
        return
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_total = calcular_costo_bitcoins(n, precio_bitcoin)
        if costo_total is not None:
            print(f"El costo actual de {n:,.4f} bitcoins en USD es: ${costo_total:,.4f}")
if __name__ == "__main__":
    main()