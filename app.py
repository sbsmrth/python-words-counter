import os
import re

class ContadorPalabras:
    def __init__(self, carpeta, palabra):
        self.carpeta = carpeta
        self.palabra = palabra
        self.resultados = {}

    def contar_palabra(self):
        try:
            archivos_txt = [archivo for archivo in os.listdir(self.carpeta) if archivo.endswith('.txt')]
            if not archivos_txt:
                return 0
            
            total_palabras = 0
            
            for archivo in archivos_txt:
                ruta_archivo = os.path.join(self.carpeta, archivo)
                with open(ruta_archivo, 'r') as file:
                    contenido = file.read()
                    contador = len(re.findall(r'\b{}\b'.format(re.escape(self.palabra)), contenido))
                    self.resultados[archivo] = contador
                    total_palabras += contador
            
            return total_palabras
        
        except FileNotFoundError:
            print("No se encuentra la carpeta indicada.")
            return 0

    def mostrar_resultados(self):
        if self.resultados:
            print("Resultados:")
            for archivo, contador in self.resultados.items():
                print(f"{archivo}: {contador} veces")
            print(f"Total: {sum(self.resultados.values())} veces")
        else:
            print("No se encontraron archivos de texto en la carpeta.")

if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")

    contador = ContadorPalabras(carpeta, palabra)
    total = contador.contar_palabra()
    contador.mostrar_resultados()

