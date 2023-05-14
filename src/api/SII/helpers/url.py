import requests

# CONSTANTES
URL_BASE = 'https://www.sii.cl/valores_y_fechas/'

# FUNCIONES AUXILIARES
#-------------------------------------------------------------------------------------------
def statusRequest(url: str):
    'Retorna el estado de conexion 200 | 404'

    try:
        urlRequest = requests.get(url)
        if(urlRequest.status_code == 200):
            return urlRequest.status_code
        else:
            print("ERROR {}: Favor revisar el dato ingresado".format(urlRequest.status_code))
            return urlRequest.status_code
    except:
        print("ERROR: La conexion ha fallado, favor validar la URL o conexion a internet.")
        return 404

def unitTypes():
    'Retorna los tipos de unidades disponibles'
    return ['uf', 'dolar']

# MAIN FUNCTION
#-------------------------------------------------------------------------------------------
def getURL(year: str, unitType: unitTypes = 'uf'):
    '''* Retorna la url de la tabla de valores del SII para el año y tipo de valor indicado.
    * Devuelve el status code de la url si no es valida.'''

    #1. Validaciones de entrada
    if unitType not in unitTypes(): 
        print('ERROR: El formato de tipo no es valido.')
        return 404

    #2. Definicion de la url
    URL = f'{URL_BASE}{unitType}/{unitType}{year}.htm'

    #3. Devolvemos el status de la url y lo evaluamos para retornar la url o el status code
    statusCode = statusRequest(URL)
    if( statusCode == 200): 
        return URL
    else:
        return statusCode