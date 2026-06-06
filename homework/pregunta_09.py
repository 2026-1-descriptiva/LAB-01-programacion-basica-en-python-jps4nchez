"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    ruta_archivo = "files/input/data.csv"
    conteo_claves = {}
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Quitamos espacios y separamos por tabulación
            columnas = linea.strip().split('\t')
            
            # Comprobamos que tenga al menos 5 columnas
            if len(columnas) > 4:
                # Extraemos la quinta columna (índice 4)
                columna_5 = columnas[4]
                
                # Separamos los distintos pares clave:valor mediante la coma
                pares = columna_5.split(',')
                
                for par in pares:
                    # Separamos por ':' y tomamos únicamente la clave (el primer elemento, índice 0)
                    clave = par.split(':')[0]
                    
                    # Sumamos 1 al conteo de esa clave en el diccionario
                    conteo_claves[clave] = conteo_claves.get(clave, 0) + 1
                    
    # Opcional: Ordenar el diccionario alfabéticamente por sus claves para que coincida 
    # visualmente con la respuesta esperada
    resultado = {clave: conteo_claves[clave] for clave in sorted(conteo_claves.keys())}
    
    return resultado

# Para probarlo:
# print(pregunta_09())
