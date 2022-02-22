# Container/Image name
FROM python:3.8

# Prepare packages
ARG PRODUCT_NAME="app"
ENV ENV="/root/.bashrc"
RUN mkdir -p /${PRODUCT_NAME}
RUN mkdir -p /etc/supervisor.d/
WORKDIR /${PRODUCT_NAME}
COPY requirements.txt .
COPY src .
COPY ./migrate.sh /docker-entrypoint-initdb.d/migrate.sh

# Install requirement
RUN pip --no-cache-dir install -r requirements.txt

# Ailas
RUN echo 'alias migrate=". /docker-entrypoint-initdb.d/migrate.sh"' >> /root/.bashrc