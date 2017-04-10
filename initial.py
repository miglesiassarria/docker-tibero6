#!/usr/bin/env python2

import urllib
import os

url = "https://github.com/miglesiassarria/tibero/raw/master/installation/Tib6.bin.00"
ruta_base = "/tibero"
destino = ruta_base + "/Tib6.bin.00"
existe = ruta_base + "/tibero6"
instalador = ruta_base + "/instalador.bin"

if os.path.exists(existe):
    print("Tibero ya se encuntra instalado")

else:
    print("INSTALANDO TIBERO")
    for i in range(5):
        urllib.urlretrieve(url + str(i+1), filename=destino + str(i+1))

    os.system("cat " + destino + "* > " + ruta_base + "/installer.bin")
    os.system("chmod +x " + ruta_base + "/instalador.bin")
    os.system(instalador + " -f /solutions/installvariables.properties -i silent")
    os.system("chmod +x /tibero/tibero6/client/bin/install.sh")
    print("Instalacion de TIBERO 6 completada")

print("Preparando scripts de base de datos")
os.system("cp /solutions/scripts/* /tibero/")
