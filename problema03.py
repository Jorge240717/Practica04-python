import requests
import zipfile
from io import BytesIO
def descargar_imagen(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Error al descargar la imagen:", response.status_code)
        return None
def guardar_zip(archivos, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as zip_file:
        for nombre_archivo, contenido in archivos.items():
            zip_file.writestr(nombre_archivo, contenido)
def unzip(nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'r') as zip_ref:
        zip_ref.extractall()
def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    imagen = descargar_imagen(url)
    if imagen:
        archivos = {"imagen.jpg": imagen}
        nombre_zip = "imagenes.zip"
        guardar_zip(archivos, nombre_zip)
        print("La imagen ha sido comprimida como", nombre_zip)
        unzip(nombre_zip)
        print("El archivo ZIP ha sido descomprimido")
if __name__ == "__main__":
    main()