FROM python:3.8.9-slim-buster as base
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential cmake git \
    libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev \
    libpq-dev curl wget vim gettext locales libmemcached-dev zlib1g-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/* \
    && locale-gen pt_BR.UTF-8 \
    && sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=pt_BR.UTF-8

FROM base
WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry export --without-hashes -f requirements.txt --output requirements.txt \
    && pip install -r requirements.txt \
    && echo "America/Sao_Paulo" > /etc/timezone \
    && ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
ENV TZ America/Sao_Paulo
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8
ENTRYPOINT ["/app/entrypoint.sh"]