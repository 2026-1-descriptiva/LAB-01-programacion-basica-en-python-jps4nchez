"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
ruta_archivo = "files/input/data.csv"

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    conteo_meses = {}
    
    # Abrimos el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Eliminamos espacios en blanco/saltos de línea y separamos por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Verificamos que existan suficientes columnas
            if len(columnas) > 2:
                fecha = columnas[2] # Tercera columna (índice 2)
                
                # Separamos la fecha por guiones ('-') y tomamos el elemento en el índice 1 (el mes)
                mes = fecha.split('-')[1]
                
                # Contamos la aparición de cada mes
                conteo_meses[mes] = conteo_meses.get(mes, 0) + 1
                
    # Retornamos la lista de tuplas ordenada alfabéticamente (por orden numérico del mes en este caso)
    resultado = sorted(conteo_meses.items())
    
    return resultado


