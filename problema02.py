import pyfiglet
import random
def obtener_fuentes_disponibles():
    return pyfiglet.FigletFont.getFonts()
def obtener_fuente_aleatoria():
    fuentes = obtener_fuentes_disponibles()
    return random.choice(fuentes)
def obtener_fuente_usuario():
    fuente = input("Ingrese el nombre de la fuente que desea utilizar (deje en blanco para elegir aleatoriamente): ").strip()
    return fuente if fuente else obtener_fuente_aleatoria()
def obtener_texto_usuario():
    return input("Ingrese el texto que desea imprimir: ")
def imprimir_texto_con_fuente(texto, fuente):
    figura = pyfiglet.Figlet(font=fuente)
    resultado = figura.renderText(texto)
    print(resultado)
def main():
    fuente = obtener_fuente_usuario()
    texto = obtener_texto_usuario()
    imprimir_texto_con_fuente(texto, fuente)
if __name__ == "__main__":
    main()