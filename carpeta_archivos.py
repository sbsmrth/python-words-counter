import os
import sys
from elemento_archivo import ElementoArchivo

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

    def listar_archivos(self):
        """
        Lista los archivos en la carpeta y los almacena en la lista 'archivos'.
        """
        try:
            for archivo in os.listdir(self.nombre):
                if archivo.endswith((".txt", ".xml", ".json", ".csv")):
                    self.archivos.append(
                        ElementoArchivo(os.path.join(self.nombre, archivo))
                    )
            if not self.archivos:
                print("No se encontraron archivos txt, xml, json, csv en la carpeta.")
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
