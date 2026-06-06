"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ('B', 4, 4),
     ...
    """
    ruta_archivo = "files/input/data.csv"
    resultado = []
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminamos espacios/saltos y separamos por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Verificamos que existan las 5 columnas
            if len(columnas) > 4:
                letra = columnas[0]
                
                # La cuarta columna (índice 3) tiene letras separadas por comas (ej. 'b,g,f')
                columna_4 = columnas[3]
                # Contamos cuántos elementos hay separando por coma
                cantidad_col4 = len(columna_4.split(','))
                
                # La quinta columna (índice 4) tiene pares clave:valor separados por comas
                columna_5 = columnas[4]
                # Contamos cuántos elementos (pares) hay separando por coma
                cantidad_col5 = len(columna_5.split(','))
                
                # Añadimos la tupla a la lista de resultados
                resultado.append((letra, cantidad_col4, cantidad_col5))
                
    return resultado

# Para probarlo:
# print(pregunta_10())
