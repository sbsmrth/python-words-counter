import os
import re
import sys

class ElementoArchivo:
    def __init__(self, nombre):
        self.nombre = nombre

class ArchivoTexto(ElementoArchivo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.contenido = ""

    def leer_contenido(self):
        try:
            with open(self.nombre, 'r') as file:
                self.contenido = file.read()
        except FileNotFoundError:
            print(f"El archivo {self.nombre} no se encuentra.")
            self.contenido = ""

    def contar_palabra(self, palabra):
        return len(re.findall(r'\b{}\b'.format(re.escape(palabra)), self.contenido))

class CarpetaArchivos(ElementoArchivo):
    def __init__(self, ruta):
        super().__init__(ruta)
        self.archivos = []

    def listar_archivos_txt(self):
        try:
            for archivo in os.listdir(self.nombre):
                if archivo.endswith('.txt'):
                    self.archivos.append(ArchivoTexto(os.path.join(self.nombre, archivo)))
            if not self.archivos:
                print("No se encontraron archivos de texto en la carpeta.")
        except FileNotFoundError:
            print(f"No se encontró la carpeta {self.nombre}.")

            sys.exit()

    def contar_palabra_en_archivos(self, palabra):
        total_palabras = 0
        for archivo in self.archivos:
            archivo.leer_contenido()
            total_palabras += archivo.contar_palabra(palabra)
        return total_palabras

class AnalizadorArchivos:
    def __init__(self, carpeta):
        self.carpeta = CarpetaArchivos(carpeta)

    def analizar(self, palabra):
        self.carpeta.listar_archivos_txt()
        total_palabras = self.carpeta.contar_palabra_en_archivos(palabra)
        self.mostrar_resultados(total_palabras)

    def mostrar_resultados(self, total):
        print("Resultados:")
        for archivo in self.carpeta.archivos:
            print(f"{archivo.nombre}: {archivo.contar_palabra(palabra)} veces")
        print(f"Total: {total} veces")

if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")

    analizador = AnalizadorArchivos(carpeta)
    analizador.analizar(palabra)
