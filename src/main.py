from SII.UnidadFomento import UnidadFomento
from SII.ScrapingSII import ScrapingSII


def main():
    uf = UnidadFomento()
    uf.date = [2013, 1, 1]
    url = uf.getUrl()
    
    if(uf.isValidUrl(url)):
        scrap = ScrapingSII(url)
        scrap.getDataScrap(date=uf.date)

if __name__ == "__main__":
    main()
