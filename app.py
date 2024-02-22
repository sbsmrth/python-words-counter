import os
import re
import sys

class ElementoArchivo:
    """
    Clase base para representar un elemento de archivo genérico.
    """
    def __init__(self, nombre):
        """
        Inicializa un nuevo elemento de archivo con el nombre dado.

        Args:
            nombre (str): El nombre del archivo o carpeta.
        """
        self.nombre = nombre

class ArchivoTexto(ElementoArchivo):
    """
    Clase para representar un archivo de texto y realizar operaciones en él.
    """
    def __init__(self, nombre):
        """
        Inicializa un nuevo archivo de texto con el nombre dado.

        Args:
            nombre (str): El nombre del archivo de texto.
        """
        super().__init__(nombre)
        self.contenido = ""

    def leer_contenido(self):
        """
        Lee el contenido del archivo de texto y lo almacena en el atributo 'contenido'.
        """
        try:
            with open(self.nombre, 'r') as file:
                self.contenido = file.read()
        except FileNotFoundError:
            print(f"El archivo {self.nombre} no se encuentra.")
            self.contenido = ""

    def contar_palabra(self, palabra):
        """
        Cuenta el número de ocurrencias de una palabra en el contenido del archivo de texto.

        Args:
            palabra (str): La palabra que se desea buscar.

        Returns:
            int: El número de ocurrencias de la palabra en el archivo de texto.
        """
        return len(re.findall(r'\b{}\b'.format(re.escape(palabra)), self.contenido))

class CarpetaArchivos(ElementoArchivo):
    """
    Clase para representar una carpeta que contiene archivos de texto y realizar operaciones en ellos.
    """
    def __init__(self, ruta):
        """
        Inicializa una nueva carpeta de archivos con la ruta dada.

        Args:
            ruta (str): La ruta de la carpeta.
        """
        super().__init__(ruta)
        self.archivos = []

    def listar_archivos_txt(self):
        """
        Lista los archivos de texto en la carpeta y los almacena en la lista 'archivos'.
        Muestra un mensaje si no se encuentran archivos de texto en la carpeta.
        """
        try:
            for archivo in os.listdir(self.nombre):
                if archivo.endswith('.txt'):
                    self.archivos.append(ArchivoTexto(os.path.join(self.nombre, archivo)))
            if not self.archivos:
                print("No se encontraron archivos de texto en la carpeta.")
                sys.exit()
        except FileNotFoundError:
            print(f"No se encontró la carpeta {self.nombre}.")
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
        Inicializa un nuevo analizador de archivos con la carpeta dada.

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
        print(f"Total: {total} veces")

if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")

    analizador = AnalizadorArchivos(carpeta)
    analizador.analizar(palabra)
