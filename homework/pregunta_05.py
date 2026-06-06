"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
ruta_archivo = "files/input/data.csv"

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    valores = {}
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminamos espacios en blanco y separamos por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Comprobamos que tenga los datos necesarios
            if len(columnas) > 1 and columnas[0] != '':
                letra = columnas[0]
                valor = int(columnas[1])
                
                # Si la letra no está en el diccionario, creamos una lista vacía para ella
                if letra not in valores:
                    valores[letra] = []
                    
                # Añadimos el valor numérico a la lista correspondiente a la letra
                valores[letra].append(valor)
                
    # Creamos la lista de tuplas con (letra, maximo, minimo) ordenando las letras alfabéticamente
    resultado = []
    for letra in sorted(valores.keys()):
        maximo = max(valores[letra])
        minimo = min(valores[letra])
        resultado.append((letra, maximo, minimo))
        
    return resultado

# Para probarlo:
# print(pregunta_05())