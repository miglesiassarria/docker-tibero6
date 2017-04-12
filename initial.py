#!/usr/bin/env python2

import urllib
import os

url = "https://github.com/miglesiassarria/tibero/raw/master/installation/Tib6.bin.00"
ruta_base = "tibero"
destino = ruta_base + "/Tib6.bin.00"
existe = ruta_base + "/tibero6"
instalador = ruta_base + "/installer.bin"
tbhome = os.environ.get("TB_HOME")


if os.path.exists(existe):
    print("Tibero ya se encuntra instalado")
    bd_list = os.listdir(tbhome)

    for name in bd_list:
        if name[(len(name)-5):len(name)] == ".conf":
            id = name[0:len(name)-5]
            os.environ["TB_SID"] = id
            os.system("tbdown clean")
            os.system("tbboot")
            # print(id)
            # print(name[(len(name)-4):len(name)])


else:
    print("INSTALANDO TIBERO")
    for i in range(5):
        urllib.urlretrieve(url + str(i+1), filename=destino + str(i+1))

    os.system("cat " + destino + "* > " + ruta_base + "/installer.bin")
    os.system("chmod +x " + ruta_base + "/installer.bin")
    os.system(instalador + " -f /solutions/installvariables.properties -i silent")
    os.system("chmod +x /tibero/tibero6/client/bin/install.sh")
    os.system("mkdir " + ruta_base + "/scripts")
    os.system("mkdir " + ruta_base + "/dbrepo")
    os.system("touch " + ruta_base + "/dbrepo/dbs.ini")

    print("Preparando scripts de base de datos")
    os.system("cp /solutions/scripts/*.sh /tibero/")
    os.system("cp /solutions/scripts/*.py /tibero/scripts")
    os.system("rm " + ruta_base + "/*bin*")

    print("INSTALACION FINALIZADA !!!DISFRUTALA!!!")
