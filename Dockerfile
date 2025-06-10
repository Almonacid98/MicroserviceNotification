FROM python:3.12-slim-bookworm
ENV TZ=America/Argentina/Mendoza

ENV FLASK_CONTEXT=production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flaskapp/.local/bin

RUN useradd --create-home --home-dir /home/flaskapp flaskapp \
    && apt-get update \
    && apt-get install -y build-essential libpq-dev curl iputils-ping \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /user/share/zoneinfo/America/Argentina/Mendoza /etc/localtime \
    && echo America/Argentina/Mendoza > /etc/timezone

WORKDIR /home/flaskapp

USER flaskapp
RUN mkdir app

COPY ./app ./app
COPY ./app.py .
COPY ./uwsgi.ini .

ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["uwsgi", "--wsgi-file","app.py", "uwsgi.ini"]
#CMD [ "python", "./app.py" ]