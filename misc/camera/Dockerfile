FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:$$cMoNm4nduNtge55ThISpAssW0rdD$$' | chpasswd
RUN useradd camera
RUN echo 'camera:ismart12' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN mkdir /home/camera
COPY flag.txt /home/camera/flag.txt

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

RUN chown -R root /home
RUN chmod -R 755 /home
