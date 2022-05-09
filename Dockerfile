FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /usr/local/lib/python3.8/

ENV APP_ROOT /src
RUN mkdir /src;
WORKDIR ${APP_ROOT}

RUN mkdir /config
ADD ./config/requirements.txt /config/
RUN pip install -U pip; \
    pip install -Ur /config/requirements.txt

ADD src ${APP_ROOT}

EXPOSE 8888

CMD python ${APP_ROOT}/main.py
