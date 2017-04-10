FROM nfqsolutions/centos:7

MAINTAINER solutions@nfq.com

# Instalacion de paquetes
RUN yum install -y java-1.7.0-openjdk && \
    mkdir /solutions/scripts

# Arreglo del error del semaforo
#RUN sysctl -w kernel.sem="10000 32000 10000 10000"

ADD initial.py /solutions/
ADD installvariables.properties /solutions/
ADD entry.sh /solutions/
ADD scripts/* /solutions/scripts/

RUN chmod +x /solutions/initial.py && \
    chmod +x /solutions/entry.sh && \
    chmod 777 -R /solutions/scripts

CMD ["/usr/bin/supervisord"]