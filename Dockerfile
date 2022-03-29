FROM python:3.9-slim-buster
ADD git-quality-check.py /

# RUN pip install pystrich

RUN apt-get upgrade -y
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN apt-get upgrade -y
RUN apt-get update
RUN apt-add-repository ppa:git-core/ppa -y
RUN apt-get -y install git
ENTRYPOINT [ "python", "/git-quality-check.py" ]