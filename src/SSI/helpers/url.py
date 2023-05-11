import requests
URL_BASE = 'https://www.sii.cl/valores_y_fechas/'

# VALIDACIONES DE ENTRADA
def isValidYear(year: str):
    'La fecha mínima que se puede consultar es el 01-01-2013, y no hay fecha máxima, ya que la tabla se actualiza constantemente.'
    
    if len(year) != 4: return False
    if int(year) < 2013: return False
    return True


def statusRequest(url: str):
    'Retorna True si la url es válida, False en caso contrario.'

    try:
        urlRequest = requests.get(url)
        return urlRequest.status_code
    except:
        return urlRequest.status_codes.codes['not_found']


# MAIN FUNCTION
def get_url(year: str, type: str = 'uf'):
    'Retorna la url de la tabla de valores del SII para el año y tipo de valor indicado.'

    #1. Validaciones de entrada
    if not isValidYear(year): return None
    if type not in ['uf', 'utm', 'dolar']: return None

    #2. Definicion de la url
    URL = f'{URL_BASE}{type}/{type}{year}.htm'

    #3. Devolvemos el status de la url
    return statusRequest(URL)