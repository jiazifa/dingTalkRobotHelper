FROM python:3.8.3

ARG pypi_host=pypi.douban.com
ARG pypi_mirror=http://pypi.douban.com/simple

ENV LC_ALL C.UTF-8

ENV LANG C.UTF-8

ENV PIP_INDEX_URL $pypi_mirror

ENV FLASK_ENV production

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip --trusted-host pypi.douban.com

RUN pip install --no-cache-dir -r requirements.txt --trusted-host ${pypi_host}

COPY app.py app.py

COPY templates templates

COPY static static

COPY local_setting.py local_setting.py

COPY start_server.sh start_server.sh

RUN chmod a+x start_server.sh

EXPOSE 5000