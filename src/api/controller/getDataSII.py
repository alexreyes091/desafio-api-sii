from SII.UnidadFomento import UnidadFomento
from SII.ScrapingSII import ScrapingSII
from SII.DateSII import DateSII


def evaluateDate(date):
    'Evalua si la fecha ingresada es valida'
    # 1. Instanciamos el objeto DateSII para poder usar sus metodos
    newDate = DateSII()
    # 2. Evaluamos si la fecha ingresada es valida
    if(newDate.isValidDate(date=date)):
        return True
    else:
        return False


def formattedDate(date):
    'Formatea la fecha ingresada a una lista con el formato [YYYY, MM, DD]'
    # 1. Instanciamos el objeto DateSII para poder usar sus metodos
    newDate = DateSII()
    
    # 2. Convertimos la fecha ingresada en una lista de enteros
    date = date.split("-")
    date = [int(i) for i in date]
    
    # 3. Formateamos la fecha ingresada
    newDate.year = date[0]
    newDate.month = date[1]
    newDate.day = date[2]
    
    # 4. Retornamos la fecha formateada
    return newDate.formatDate


def getDataSII(date, typeSearch = 'day', unitFoment = 'uf'):
    'Devuelve el valor de la unidad de fomento para la fecha ingresada.'

    # 1. Evaluamos si la fecha ingresada es valida
    if(evaluateDate(date)):
        # 2. Instanciamos el objeto UnidadFomento, definimos la fecha y la url
        uf = UnidadFomento()
        uf.date = formattedDate(date)

        # 3. Evaluamos si la fecha cumple con los requisitos de SII
        if(uf.isValidDate()) == False:
            return {"ERROR": f"La fecha ingresada debe ser mayor a la fecha minima definida: {uf.minDate.formatDate}"} 

        # 4. Obtenemos la url
        url = uf.getUrl(unitType = unitFoment)

        if not url == 404:
            # 5. Instanciamos el objeto ScrapingSII y obtenemos los datos
            scrap = ScrapingSII(url)
            data = scrap.getScrap(date=uf.date, typeSearch = typeSearch)

            # 6. Retornamos los datos
            return data
        else:
            return {"ERROR": "Registro no encontrado, favor validar la URL ingresada."}

    else:
        return {"ERROR": "La fecha ingresada no es valida, debe estar en formato YYYY-MM-DD, incluyendo los guiones ( - )."}
