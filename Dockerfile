FROM nfqsolutions/centos:7

MAINTAINER solutions@nfq.com

# Instalacion de paquetes
RUN yum install -y java-1.7.0-openjdk

# Arreglo del error del semaforo
RUN sysctl -w kernel.sem="10000 32000 10000 10000"

CMD ["/usr/bin/supervisord"]