# https://docs.docker.com/develop/develop-images/multistage-build/
FROM quay.io/blueshoe/python3.9-slim AS builder

LABEL vendor="Blueshoe GmbH"

ENV POETRY_VERSION=1.1.5 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  PATH="$PATH:/root/.poetry/bin"

WORKDIR /app

COPY . /app
RUN mkdir -p /var/www/static/

# Project initialization:
RUN apt-get update && apt-get upgrade -y
RUN apt-get install --no-install-recommends -y curl
RUN curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python
RUN poetry install --no-interaction --no-ansi
RUN python manage.py collectstatic

CMD python manage.py serve --autoreload --static