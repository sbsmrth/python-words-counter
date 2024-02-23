import re

class ElementoArchivo():
    """
    Clase para representar un archivo y realizar operaciones en él.
    """
    def __init__(self, nombre):
        """
        Inicializa un nuevo archivo con el nombre dado.

        Args:
            nombre (str): El nombre del archivo
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