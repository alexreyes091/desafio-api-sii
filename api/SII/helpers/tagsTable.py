
def getTagOfTable(month: int):

    listMonths = {
        0:'mes_all',
        1:'mes_enero',
        2:'mes_febrero',
        3:'mes_marzo',
        4:'mes_abril',
        5:'mes_mayo',
        6:'mes_junio',
        7:'mes_julio',
        8:'mes_agosto',
        9:'mes_septiembre',
        10:'mes_octubre',
        11:'mes_noviembre',
        12:'mes_diciembre',
    }

    return listMonths.get(month)