"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    ruta_archivo = "files/input/data.csv"
    sumas_letras = {}
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            
            # Verificamos que tenga al menos 4 columnas
            if len(columnas) > 3:
                # Obtenemos el valor de la columna 2 y lo convertimos a entero
                valor = int(columnas[1])
                
                # Obtenemos las letras de la columna 4 y las separamos por coma
                letras = columnas[3].split(',')
                
                # Para cada letra encontrada en esa fila, le sumamos el valor de la columna 2
                for letra in letras:
                    sumas_letras[letra] = sumas_letras.get(letra, 0) + valor
                    
    # Construimos un nuevo diccionario con las claves ordenadas alfabéticamente
    resultado = {clave: sumas_letras[clave] for clave in sorted(sumas_letras.keys())}
    
    return resultado

# Para probarlo:
# print(pregunta_11())
