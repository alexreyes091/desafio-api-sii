
def getMonth(month: int):

    listMonths = {
        0:'ALL_MONTHS',
        1:'MES_ENERO',
        2:'MES_FEBRERO',
        3:'MES_MARZO',
        4:'MES_ABRIL',
        5:'MES_MAYO',
        6:'MES_JUNIO',
        7:'MES_JULIO',
        8:'MES_AGOSTO',
        9:'MES_SEPTIEMBRE',
        10:'MES_OCTUBRE',
        11:'MES_NOVIEMBRE',
        12:'MES_DICIEMBRE',
    }

    return listMonths.get(month)