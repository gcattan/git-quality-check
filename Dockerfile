FROM python:3.9-slim-buster
ADD git-quality-check.py /

# RUN pip install pystrich

RUN apt-get update && apt-get -y install git
ENTRYPOINT [ "python", "/git-quality-check.py" ]