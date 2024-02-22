import os
import re
import sys

class ArchivoTexto:
    """
    Clase para representar un archivo de texto y realizar operaciones en él.
    """
    def __init__(self, nombre):
        """
        Inicializa un objeto ArchivoTexto con un nombre de archivo dado.

        Args:
            nombre (str): El nombre del archivo.
        """
        self.nombre = nombre
        self.contenido = ""

    def leer_contenido(self):
        """
        Lee el contenido del archivo y lo almacena en el atributo 'contenido'.
        """
        try:
            with open(self.nombre, 'r') as file:
                self.contenido = file.read()
        except FileNotFoundError:
            print(f"El archivo {self.nombre} no se encuentra.")
            self.contenido = ""

    def contar_palabra(self, palabra):
        """
        Cuenta el número de ocurrencias de una palabra en el contenido del archivo.

        Args:
            palabra (str): La palabra que se desea buscar.

        Returns:
            int: El número de ocurrencias de la palabra en el archivo.
        """
        return len(re.findall(r'\b{}\b'.format(re.escape(palabra)), self.contenido))

class CarpetaArchivos:
    """
    Clase para representar una carpeta que contiene archivos de texto y realizar operaciones en ellos.
    """
    def __init__(self, ruta):
        """
        Inicializa un objeto CarpetaArchivos con la ruta de la carpeta dada.

        Args:
            ruta (str): La ruta de la carpeta.
        """
        self.ruta = ruta
        self.archivos = []

    def listar_archivos_txt(self):
        """
        Lista los archivos de texto en la carpeta y los almacena en la lista 'archivos'.
        """
        try:
            for archivo in os.listdir(self.ruta):
                if archivo.endswith('.txt'):
                    self.archivos.append(ArchivoTexto(os.path.join(self.ruta, archivo)))
        except FileNotFoundError:
            print(f"No se encontró la carpeta {self.ruta}.")
            sys.exit()

    def contar_palabra_en_archivos(self, palabra):
        """
        Cuenta el número total de ocurrencias de una palabra en todos los archivos de la carpeta.

        Args:
            palabra (str): La palabra que se desea buscar.

        Returns:
            int: El número total de ocurrencias de la palabra en todos los archivos.
        """
        total_palabras = 0
        for archivo in self.archivos:
            archivo.leer_contenido()
            total_palabras += archivo.contar_palabra(palabra)
        return total_palabras

class AnalizadorArchivos:
    """
    Clase para analizar archivos de texto en una carpeta dada en busca de una palabra específica.
    """
    def __init__(self, carpeta):
        """
        Inicializa un objeto AnalizadorArchivos con la carpeta dada.

        Args:
            carpeta (str): La ruta de la carpeta que se va a analizar.
        """
        self.carpeta = CarpetaArchivos(carpeta)

    def analizar(self, palabra):
        """
        Analiza los archivos de la carpeta en busca de una palabra específica y muestra los resultados.

        Args:
            palabra (str): La palabra que se desea buscar.
        """
        self.carpeta.listar_archivos_txt()
        total_palabras = self.carpeta.contar_palabra_en_archivos(palabra)
        self.mostrar_resultados(total_palabras)

    def mostrar_resultados(self, total):
        """
        Muestra los resultados del análisis, incluyendo el número de ocurrencias de la palabra en cada archivo y el total.

        Args:
            total (int): El número total de ocurrencias de la palabra en todos los archivos.
        """
        print("Resultados:")
        for archivo in self.carpeta.archivos:
            print(f"{archivo.nombre}: {archivo.contar_palabra(palabra)} veces")
        
        if len(self.carpeta.archivos) == 0:
            print("No se encontraron archivos de texto en la carpeta.")

        print(f"Total: {total} veces")

if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")

    analizador = AnalizadorArchivos(carpeta)
    analizador.analizar(palabra)
