"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

ruta_archivo = "files/input/data.csv"

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    sumas = {}
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Limpiamos los saltos de línea y separamos por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Verificamos que la línea tenga la estructura correcta
            if len(columnas) > 1 and columnas[0] != '':
                letra = columnas[0]
                valor = int(columnas[1])
                
                # Acumulamos el valor en la clave correspondiente a la letra
                sumas[letra] = sumas.get(letra, 0) + valor
                
    # Retornamos la lista de tuplas ordenada alfabéticamente por la letra
    resultado = sorted(sumas.items())
    
    return resultado

