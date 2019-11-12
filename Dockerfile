FROM alpine

LABEL mantainer="pueblafran@gmail.com"

ENV TERM xterm

RUN apk update
RUN apk add python py2-pip uwsgi uwsgi-python py-mysqldb
RUN mkdir -p /opt/shogi
WORKDIR /opt/shogi
COPY src/ /opt/shogi/

RUN pip install --upgrade pip
RUN pip install -U setuptools
RUN pip install -r requirements.txt

USER 1000:1000

CMD uwsgi --ini /opt/shogi/shogi.ini

EXPOSE 8000
