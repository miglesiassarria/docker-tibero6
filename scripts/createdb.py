import os
import ConfigParser

conf_file = os.environ['INSTALL_HOME'] + "/dbrepo/dbs.ini"

config = ConfigParser.ConfigParser()
config.read(conf_file)
lista = []


def file_write(db, port):
    cfgfile = open(conf_file, "w")
    config.add_section(new_db)
    config.set(db, "puerto", port)
    config.write(cfgfile)
    cfgfile.close()


def get_ports():
    for seccione in config.sections():
        lista.append(config.get(seccione, "puerto"))
    return lista


print("BASES DE DATOS EXISTENTES:")
print(config.sections())
# print(len(config.sections()))

new_db = raw_input("INTRODUCE UN NOMBRE PARA TU NUEVA BASE DE DATOS: ")
if new_db in config.sections():
    print("ESA BASE DE DATOS YA EXISTE. ADIOS")

else:
    print("Estos son los puertos ya ocupados: ")
    print(get_ports())
    new_port = raw_input("INTRODUCE EL PUERTO LIBRE ENTRE 8629-8639 PARA LA BASE DE DATOS " + new_db + ":  ")

    if new_port in get_ports():
        print("PUERTO YA OCUPADO ADIOS")

    else:
        file_write(new_db, new_port)
        # os.system("install.sh")
        print("BASE DE DATOS CREADA")


# get_ports()
# print(lista)
