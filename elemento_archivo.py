
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