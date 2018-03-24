FROM python:2.7

ENV HOME /home/jfantom

WORKDIR $HOME

RUN apt-get -qq update &&\
    apt-get -qq install -y \
    supervisor vim curl wget

COPY jfantom_ui $HOME/jfantom_ui
COPY scripts $HOME/scripts
COPY config $HOME/config 

RUN pip install \
    -e $HOME/jfantom_ui

ENTRYPOINT [\
   "gunicorn", \
   "--bind", "0.0.0.0:8000", \
   "--worker-class", "eventlet", \
   "--access-logfile", "-", \
   "--workers", "4", \
   "--log-level", "debug", \
   "jfantom_ui.main:app" ]