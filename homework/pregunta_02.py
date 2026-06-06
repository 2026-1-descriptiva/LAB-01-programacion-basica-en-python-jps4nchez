"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
ruta_archivo = "files/input/data.csv"

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    conteo = {}
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminamos los espacios o saltos de línea y dividimos por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Verificamos que la línea no esté vacía
            if len(columnas) > 0 and columnas[0] != '':
                letra = columnas[0]
                
                # Si la letra ya está en el diccionario, sumamos 1. Si no, la agregamos con valor 1.
                conteo[letra] = conteo.get(letra, 0) + 1
                
    # La función items() obtiene las tuplas (clave, valor) y sorted() las ordena alfabéticamente por la clave
    resultado = sorted(conteo.items())
    
    return resultado

