FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
COPY . /code/

COPY entrypoint.sh /usr/bin
RUN chmod +x /usr/bin/entrypoint.sh
CMD [ "entrypoint.sh" ]