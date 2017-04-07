import urllib
import os.path
import os

url = "https://github.com/miglesiassarria/tibero/raw/master/installation/Tib6.bin.00"
destino = "tibero/Tib6.bin.00"
existe = "tibero/tibero6"

if os.path.exists(existe):
    print("Tibero ya se encuntra instalado")

else:
    print("INSTALANDO TIBERO")
    for i in range(5):
        urllib.urlretrieve(url + str(i+1), filename=destino + str(i+1))


    os.system("cat /tibero/*.bin* > /tibero/installer")



# os.system("wget --no-check-certificate --content-disposition https://github.com/miglesiassarria/tibero/raw/master/installation/Tib6.bin.001 -O tibero/Tib6.bin.001")