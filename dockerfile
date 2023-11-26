FROM ubuntu:22.04
WORKDIR /tmp
ENV TCP_PORT=10500,9999
COPY ./script/* /tmp/
RUN apt update && apt install -y python3 vsftpd systemctl net-tools openssh-server vim lsof\
    && useradd -m ftpuser && echo 'ftpuser:huawei' | chpasswd && mkdir /var/run/sshd
CMD [ "/bin/bash", "-c", "/tmp/start.sh"]
