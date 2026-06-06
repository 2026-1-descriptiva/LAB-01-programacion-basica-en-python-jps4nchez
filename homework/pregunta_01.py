"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
ruta_archivo = "files/input/data.csv"

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    
    Rta/
    214
    """
    suma_total = 0
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminamos los espacios en blanco o saltos de línea al final y dividimos por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Verificamos que la línea tenga al menos dos columnas para evitar errores
            if len(columnas) > 1:
                # Convertimos el valor de la segunda columna (índice 1) a entero y lo sumamos
                suma_total += int(columnas[1])
                
    return suma_total

