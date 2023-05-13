import requests

# CONSTANTES
URL_BASE = 'https://www.sii.cl/valores_y_fechas/'

# FUNCIONES AUXILIARES
def statusRequest(url: str):
    'Retorna el estado de conexion 200 | 404'

    try:
        urlRequest = requests.get(url)
        return urlRequest.status_code
    except:
        print("ERROR: La conexion ha fallado, favor validar la URL o conexion a internet.")
        return 404

# MAIN FUNCTION
def getURL(year: str, type: str = 'uf'):
    'Retorna la url de la tabla de valores del SII para el año y tipo de valor indicado.'

    #1. Validaciones de entrada
    if type not in ['uf', 'utm', 'dolar']: 
        print('ERROR: El formato de tipo no es valido.')
        return None

    #2. Definicion de la url
    URL = f'{URL_BASE}{type}/{type}{year}.htm'

    #3. Devolvemos el status de la url y lo evaluamos para retornar la url o None
    if(statusRequest(URL) == 200): 
        return URL
    else:
        return None