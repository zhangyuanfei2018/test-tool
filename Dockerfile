FROM python:3.9.7

MAINTAINER zyf "1398174363@qq.com"

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8010"]