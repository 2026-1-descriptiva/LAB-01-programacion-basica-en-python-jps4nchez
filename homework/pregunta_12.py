"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    ruta_archivo = "files/input/data.csv"
    sumas_por_letra = {}
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Quitamos los espacios en blanco y dividimos la línea por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Comprobamos que existan las 5 columnas requeridas
            if len(columnas) > 4:
                # Extraemos la letra de la primera columna
                letra = columnas[0]
                
                # Extraemos la cadena de la quinta columna y separamos los pares por coma
                pares = columnas[4].split(',')
                
                # Variable para sumar los valores numéricos de esta línea
                suma_fila = 0
                
                for par in pares:
                    # Separamos cada par por los dos puntos y tomamos el valor (índice 1)
                    valor_str = par.split(':')[1]
                    suma_fila += int(valor_str)
                    
                # Acumulamos la suma de la fila en el registro correspondiente a la letra
                sumas_por_letra[letra] = sumas_por_letra.get(letra, 0) + suma_fila
                
    # Retornamos el diccionario ordenando las claves (letras) alfabéticamente
    resultado = {clave: sumas_por_letra[clave] for clave in sorted(sumas_por_letra.keys())}
    
    return resultado

# Para probarlo:
# print(pregunta_12())
