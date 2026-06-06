"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    ruta_archivo = "files/input/data.csv"
    
    agrupacion = {}
    
    # Abrimos el archivo
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            
            if len(columnas) > 1 and columnas[0] != '':
                letra = columnas[0]
                # Convertimos el valor numérico a entero para que se ordene correctamente luego
                numero = int(columnas[1])
                
                # Si el número aún no es una clave en el diccionario, inicializamos una lista vacía
                if numero not in agrupacion:
                    agrupacion[numero] = []
                    
                # Añadimos la letra a la lista correspondiente a ese número
                agrupacion[numero].append(letra)
                
    # La función items() nos da tuplas (numero, [letras]) y sorted() las ordena de menor a mayor por la clave (el número)
    resultado = sorted(agrupacion.items())
    
    return resultado

# Para probarlo:
# print(pregunta_07())