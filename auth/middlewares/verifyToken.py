from fastapi import Request
from fastapi.routing import APIRoute
from auth.jwt.funJWT import validateToken

class VerifyTokenRoute(APIRoute):
    def getRouteHandler(self):
        origin = super().getRouteHandler()
        
        async def verifyTokenMiddleware(request: Request):
            token = request.headers["Authorization"].split(" ")[1]

            validateResponse = validateToken(token, output=False)

            if validateToken == None:
                return await origin(request)
            else:   
                return validateToken
            