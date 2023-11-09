from ftplib import FTP_TLS
import io
import sys
import gzip

def pobierz_efemeryde(rok=2023, nazwa='brdc.n'):
    ftps = FTP_TLS(host = 'gdc.cddis.eosdis.nasa.gov')
    ftps.login(user='anonymous', passwd="")
    ftps.prot_p()
    
    # ftp://gdc.cddis.eosdis.nasa.gov/pub/gps/data/daily/2023/brdc/brdc3120.23n.gz
    ftps.cwd(f"/pub/gps/data/daily/{rok}/brdc/")
    files = ftps.nlst()

    filename = None
    unzipfn = nazwa

    for fn in files[::-1]:
        if fn[-4:]=='n.gz':
            filename = fn
            break
    if filename == None:
        print("błąd pobierania efemerydy")
        exit()


    ftps.retrbinary("RETR " + filename, open(filename, 'wb').write)
    with gzip.open(filename, 'rb') as f:
        with open(unzipfn, 'wb') as uf:
            uf.write(f.read())

def main():
    pobierz_efemeryde()

if __name__=="__main__":
    main()
