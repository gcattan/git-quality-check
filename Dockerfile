FROM python:3.9-slim-buster
ADD git_quality_check /git_quality_check
ADD example /example
ADD setup.py /
ADD README.md /

RUN apt-get update
RUN apt-get -y install git

RUN python setup.py develop

ENTRYPOINT [ "python", "/example/git-quality-check.py" ]