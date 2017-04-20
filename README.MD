**REQUERIMIENTOS DEL CONTENEDOR:**

- Es necesario que este activado el modo privilegiado para evitar el problema del semaforo.
- Es necesario tener un volumen montado que apuntará a /tibero yy donde se realizará toda la instalación.
 En este directorio hemos de meter nuestra liciencia.
- Es necesario ejecutar en el anfitrión el siguiente comando para arreglar el problema del semaforo:
sysctl -w kernel.sem="10000 32000 10000 10000"