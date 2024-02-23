import re
from elemento_archivo import ElementoArchivo

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