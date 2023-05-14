from fastapi import APIRouter
from controller.getDataSII import getDataSII

router = APIRouter(prefix="/api",
                tags=["Scraping SII"],
                responses={404: {"description": "Not found in SII"}})

@router.get("/sii/date/{typeSearch}/{unitFoment}/{date}")
async def dataSII(date: str, typeSearch = str, unitFoment = str):
    return getDataSII(date, typeSearch, unitFoment)