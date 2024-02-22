import os

def contar_palabra_en_archivos(carpeta, palabra):
    if not os.path.exists(carpeta):
        print("La carpeta indicada no existe.")
        return

    total = 0
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            ruta_archivo = os.path.join(carpeta, archivo)
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                veces = contenido.lower().count(palabra.lower())
                print(f"{archivo}: {veces} veces")
                total += veces

    if total == 0:
        print("No se encontraron ocurrencias de la palabra en los archivos de texto.")
    else:
        print(f"Total: {total} veces")

if __name__ == "__main__":
    carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra = input("Ingrese la palabra que desea buscar: ")
    print("\nResultados:")
    contar_palabra_en_archivos(carpeta, palabra)
