FROM nfqsolutions/centos:7

MAINTAINER solutions@nfq.com

# Instalacion de paquetes
RUN yum install -y java-1.7.0-openjdk libaio.x86_64 && \
    mkdir /solutions/scripts

ENV TB_HOME=/tibero/tibero6 \
    INSTALL_HOME=/tibero \
    LD_LIBRARY_PATH=:/tibero/tibero6/lib:/tibero/tibero6/client/lib \
    PATH=/usr/xpg4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/bin:/usr/bin:/sbin:/usr/sbin:/usr/local/bin:/tibero/tibero6/bin:/tibero/tibero6/client/bin

ADD initial.py /solutions/
ADD installvariables.properties /solutions/
ADD InstallScript.iap_xml /solutions/
ADD entry.sh /solutions/
ADD scripts/* /solutions/scripts/

RUN chmod +x /solutions/initial.py && \
    chmod +x /solutions/entry.sh && \
    chmod 777 -R /solutions/scripts

COPY supervisord.conf /etc/supervisord.conf

CMD ["/usr/bin/supervisord"]