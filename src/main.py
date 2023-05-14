from SII.UnidadFomento import UnidadFomento
from SII.ScrapingSII import ScrapingSII
from SII.DateSII import DateSII


def main():
    uf = UnidadFomento()
    uf.date = [2023, 2, 2]
    url = uf.getUrl('uf')
    
    scrap = ScrapingSII(url)
    # searchBy = scrap.typeSearch['month']
    data = scrap.getScrap(date=uf.date, typeSearch="day")
    # print(data);
   
if __name__ == "__main__":
    main()
