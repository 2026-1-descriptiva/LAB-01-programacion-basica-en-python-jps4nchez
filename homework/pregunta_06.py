"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    ruta_archivo = "files/input/data.csv"
    valores_diccionario = {}
    
    # Abrimos el archivo utilizando la ruta especificada
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que existe la quinta columna (índice 4)
            if len(columnas) > 4:
                # Obtenemos el string de la quinta columna, ej: 'jjj:12,bbb:3,ddd:9'
                columna_5 = columnas[4]
                
                # Separamos por comas para obtener cada par 'clave:valor'
                pares = columna_5.split(',')
                
                for par in pares:
                    # Separamos por los dos puntos para dividir la clave del valor
                    clave, valor_str = par.split(':')
                    valor = int(valor_str)
                    
                    # Si la clave (ej. 'aaa') no existe, creamos una lista vacía para ella
                    if clave not in valores_diccionario:
                        valores_diccionario[clave] = []
                        
                    # Agregamos el número a la lista correspondiente a esa clave
                    valores_diccionario[clave].append(valor)
                    
    # Construimos la lista de tuplas con el formato (clave, mínimo, máximo)
    resultado = []
    # Ordenamos las claves alfabéticamente
    for clave in sorted(valores_diccionario.keys()):
        minimo = min(valores_diccionario[clave])
        maximo = max(valores_diccionario[clave])
        resultado.append((clave, minimo, maximo))
        
    return resultado

# Para probarlo:
# print(pregunta_06())
