# https://docs.docker.com/develop/develop-images/multistage-build/
FROM quay.io/blueshoe/python3.9-slim AS builder

LABEL vendor="Blueshoe GmbH"

WORKDIR /app

COPY . /app
RUN mkdir -p /var/www/static/

RUN pip3 install django==3.1.13
RUN pip3 install psycopg2-binary
RUN pip3 install graphene-django
RUN pip3 install django-hurricane
RUN python manage.py collectstatic

CMD python manage.py serve --autoreload --static