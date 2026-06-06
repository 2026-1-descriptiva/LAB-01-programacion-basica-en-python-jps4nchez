"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    ruta_archivo = "files/input/data.csv"
    agrupacion = {}
    
    # Abrimos el archivo
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            
            if len(columnas) > 1 and columnas[0] != '':
                letra = columnas[0]
                numero = int(columnas[1])
                
                # En lugar de inicializar una lista, inicializamos un conjunto (set)
                if numero not in agrupacion:
                    agrupacion[numero] = set()
                    
                # Añadimos la letra al conjunto (los conjuntos omiten duplicados automáticamente)
                agrupacion[numero].add(letra)
                
    resultado = []
    
    # Ordenamos las claves (números) para iterar de 0 a 9
    for numero in sorted(agrupacion.keys()):
        # Convertimos el conjunto a lista y la ordenamos alfabéticamente
        letras_ordenadas = sorted(list(agrupacion[numero]))
        
        # Agregamos la tupla con el formato solicitado
        resultado.append((numero, letras_ordenadas))
        
    return resultado

# Para probarlo:
# print(pregunta_08())
