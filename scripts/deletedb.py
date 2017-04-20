import os
import shutil
import time

ruta_conf = "/tibero/tibero6/"
ruta_data = ruta_conf + "database/"

sid_id = raw_input("INTRODUCE EL SID DE LA BASE DE DATOS A ELIMINAR: ")

os.environ["TB_SID"] = sid_id
os.system("tbdown")
time.sleep(9)
os.remove(ruta_conf + sid_id + ".conf")
shutil.rmtree(ruta_data + sid_id)

print("LA BASE DE DATOS " + sid_id + " HA SIDO ELIMINADA")