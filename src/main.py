from SII.UnidadFomento import UnidadFomento
from SII.ScrapingSII import ScrapingSII

def main():
    uf = UnidadFomento()
    uf.date = [2022, 12, 8]
    url = uf.getUrl()
    
    scrap = ScrapingSII(url)
    # searchBy = scrap.typeSearch['month']
    data = scrap.getScrap(date=uf.date, typeSearch="month")
    print(data);
   
if __name__ == "__main__":
    main()
