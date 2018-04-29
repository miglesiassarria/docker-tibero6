<img src="https://travis-ci.org/miglesiassarria/docker-tibero6.svg?branch=master">

**REQUERIMIENTOS DEL CONTENEDOR:**

- Es necesario tener un volumen montado que apuntará a /tibero y donde se realizará toda la instalación.
 En este directorio hemos de meter nuestra liciencia.
- En caso de error, es necesario ejecutar en el anfitrión el siguiente comando para arreglar el problema del semaforo:
sysctl -w kernel.sem="10000 32000 10000 10000"


**DOCKER-COMPOSE**

    server:
      image: nfqsolutions/tibero
      container_name: tibero
      ports:
       - "8629-8649:8629-8649"
      hostname: tibero
      volumes:
       - ./volumen:/tibero


**MODO DE USO**
===============

***CREAR UNA BBDD:***
Tras lanzar el docker-compose, tendremos tibero 6 instalado, pero no habrá ninguna base de datos creada.
En el volumen que hemos montado (ver el docker-compose) nos aparecera el script newdb.sh el cual habrá que ejecutar
con el nombre del contenedor como parametro. Ej:
 - ./newdb.sh tibero

A parir de este punto el sistema nos irá preguntando la informacion que requiere para crear la base de datos.





***BORRAR UNA BBDD:***
Es tan sencillo como ejecutar el script deletedb.sh (situado en el volumen que hemmos montado) y el nombre del contenedor como paramentro. Ej:
 - ./deletedb.sh tibero

Esto simplemente nos pedira el SID de la base de datos que queremos eliminar.
