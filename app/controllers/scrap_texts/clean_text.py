import re

def clean_text(text):
    """ Clean a text file by removing empty lines and organizing sections.
    Args:
        text (str): The path to the text file to clean.
    Returns:
        None
    Examples:
        >>> clean_text("example.txt")
    """
    
    with open(text, "r+") as archivo:
        lineas = archivo.readlines()
        secciones = []
        seccion_actual = []
        for linea in lineas:
            if linea := linea.strip():
                seccion_actual.append(linea)
            elif seccion_actual:
                secciones.append(seccion_actual)
                seccion_actual = []
        if seccion_actual:
            secciones.append(seccion_actual)
        archivo.seek(0)
        archivo.truncate()
        for seccion in secciones:
            if len(seccion) == 1:
                archivo.write(f"{seccion[0]}\n\n")
            else:
                for linea in seccion:
                    archivo.write(f" - {linea}\n")
            archivo.write("\n")