FROM ubuntu
LABEL version="1.0.0" description="Disponibilizando Python3 com Flask" maintainer="rafa@rafael.cteixeira.nom.br>"

RUN apt-get update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install flask
RUN pip3 install requests
EXPOSE 5001
#WORKDIR /api
COPY . /
CMD ls -l
CMD python3 web.py





