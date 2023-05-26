#Fastapi
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
# JWT & API
from api.SII.controller.getDataSII import getDataSII
from auth.routes.routes import oauth_schema
# Middlewares
from auth.middlewares.verifyToken import VerifyTokenRoute


router = APIRouter(route_class = VerifyTokenRoute,
                prefix="",
                tags=["Scraping SII"])

@router.get('/')
async def root():
    return RedirectResponse("/docs")


@router.get("/api/sii/date/{typeSearch}/{unitFoment}/{date}")
async def dataSII(date: str, typeSearch = str, unitFoment = str, token=Depends(oauth_schema)):
    return getDataSII(date, typeSearch, unitFoment)

