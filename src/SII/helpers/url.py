import requests

# CONSTANTES
URL_BASE = 'https://www.sii.cl/valores_y_fechas/'

# FUNCIONES AUXILIARES
def statusRequest(url: str):
    'Retorna True si la url es válida, False en caso contrario.'

    try:
        urlRequest = requests.get(url)
        return urlRequest.status_code
    except:
        return urlRequest.status_codes.codes['not_found']


# MAIN FUNCTION
def getURL(year: str, type: str = 'uf'):
    'Retorna la url de la tabla de valores del SII para el año y tipo de valor indicado.'

    #1. Validaciones de entrada
    if type not in ['uf', 'utm', 'dolar']: return None

    #2. Definicion de la url
    URL = f'{URL_BASE}{type}/{type}{year}.htm'

    #3. Devolvemos el status de la url y lo evaluamos para retornar la url o None
    if(statusRequest(URL) == 200): 
        return URL
    else:
        return None