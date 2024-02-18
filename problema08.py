import sqlite3
import requests
from datetime import datetime

# Función para obtener el tipo de cambio PEN a USD desde SUNAT
def get_pen_to_usd_exchange_rate():
    try:
        response = requests.get("https://api.apis.net.pe/v1/tipo-cambio-sunat")
        data = response.json()
        exchange_rate = data['data']['items'][0]['Tcambio']
        return float(exchange_rate)
    except Exception as e:
        print("Error al obtener el tipo de cambio PEN a USD:", e)
        return None
def get_bitcoin_prices():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        prices = {
            'USD': float(data['bpi']['USD']['rate'].replace(",", "")),
            'GBP': float(data['bpi']['GBP']['rate'].replace(",", "")),
            'EUR': float(data['bpi']['EUR']['rate'].replace(",", ""))
        }
        return prices
    except Exception as e:
        print("Error al obtener los precios de Bitcoin:", e)
        return None
def get_bitcoin_price_in_pen():
    try:
        bitcoin_prices = get_bitcoin_prices()
        usd_to_pen_exchange_rate = get_pen_to_usd_exchange_rate()
        if bitcoin_prices and usd_to_pen_exchange_rate:
            bitcoin_price_in_usd = bitcoin_prices['USD']
            bitcoin_price_in_pen = bitcoin_price_in_usd * usd_to_pen_exchange_rate
            return bitcoin_price_in_pen
        else:
            return None
    except Exception as e:
        print("Error al calcular el precio de Bitcoin en PEN:", e)
        return None
def create_bitcoin_table():
    try:
        conn = sqlite3.connect('bitcoin_database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                     (fecha TEXT, precio_usd REAL, precio_gbp REAL, precio_eur REAL, precio_pen REAL)''')
        bitcoin_prices = get_bitcoin_prices()
        bitcoin_price_in_pen = get_bitcoin_price_in_pen()
        if bitcoin_prices and bitcoin_price_in_pen:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            c.execute("INSERT INTO bitcoin VALUES (?, ?, ?, ?, ?)", (fecha, bitcoin_prices['USD'], bitcoin_prices['GBP'], bitcoin_prices['EUR'], bitcoin_price_in_pen))
            conn.commit()
        conn.close()
    except Exception as e:
        print("Error al crear la tabla 'bitcoin' y almacenar los datos:", e)
def calculate_prices():
    try:
        conn = sqlite3.connect('bitcoin_database.db')
        c = conn.cursor()
        c.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
        row = c.fetchone()
        if row:
            bitcoin_price_in_pen = row[0]
            bitcoin_price_in_eur = row[1]
            price_in_pen = bitcoin_price_in_pen * 10
            price_in_eur = bitcoin_price_in_eur * 10
            conn.close()
            return price_in_pen, price_in_eur
        else:
            print("No se encontraron datos en la tabla 'bitcoin'")
            conn.close()
            return None, None
    except Exception as e:
        print("Error al realizar la consulta y calcular los precios:", e)
        return None, None
create_bitcoin_table()
precio_en_pen, precio_en_eur = calculate_prices()
if precio_en_pen is not None and precio_en_eur is not None:
    print("Precio de comprar 10 bitcoins en PEN:", precio_en_pen)
    print("Precio de comprar 10 bitcoins en EUR:", precio_en_eur)