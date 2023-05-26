from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from jwt import encode, decode, exceptions

def expireDate(days: int):
    'Define la fecha de expiracion del token'
    
    date = datetime.now()
    new_date = date + timedelta(days=days)
    
    return new_date

def validateToken(token, output=False):
    'Valida el token para ver si es valido o devolvemos un error'

    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms=['HS256'])
        return decode(token, key=getenv("SECRET"), algorithms=['HS256'])
    except exceptions.DecodeError:
        return JSONResponse(content={"ERROR": "Token is invalid"}, status_code=401)

    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"ERROR": "User not found"}, status_code=404)


def writeToken(data: dict):
    'Escribe el token con los datos que nos pasan'
    token = encode(payload={**data, 'exp': expireDate(7)}, key='SCRAPINGSII_SECRET', algorithm='HS256')
    return token