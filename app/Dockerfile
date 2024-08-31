FROM python:3.10

ENV TZ Asia/Singapore
ENV LC_ALL=C.UTF-8
ENV export LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN python3 -m pip install setuptools
RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY src /app/

ENTRYPOINT [ "/bin/bash" , "start_app.sh"]
