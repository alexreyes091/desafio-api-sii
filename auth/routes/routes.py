# FastApi
from fastapi import FastAPI, APIRouter, Depends, Form, Header
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# JWT
from auth.jwt.funJWT import writeToken, validateToken
from auth.models.User import User

router = APIRouter(prefix="",
                tags=["Auth"],
                responses={404: {"description": "Not found in Auth"}})
        
oauth_schema = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "adminSII":
        # Simulate a user
        user = User(username=form_data.username, email="my-email@email.hn", password=form_data.password)
        # Create token
        token = writeToken(data=user.dict())
        return token
    else:
        return JSONResponse(content={"ERROR": "Incorrect username or password"}, status_code=404)


@router.post("/verify/token")
async def verify_token(Authorization: str = Header(None)):
    print(Authorization)
    return 'sucess'
    # token = Authorization.split(" ")[1]
    # return validateToken(token=token, output=False)