from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from SII.controller.getDataSII import getDataSII

router = APIRouter(prefix="",
                tags=["Scraping SII"],
                responses={404: {"description": "Not found in SII"}})

@router.get('/')
async def root():
    return RedirectResponse("/docs")


@router.get("/api/sii/date/{typeSearch}/{unitFoment}/{date}")
async def dataSII(date: str, typeSearch = str, unitFoment = str):
    return getDataSII(date, typeSearch, unitFoment)

