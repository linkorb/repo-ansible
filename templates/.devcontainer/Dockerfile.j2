# [Choice] PHP version (use -bullseye variants on local arm64/Apple Silicon): 8, 8.1, 8.0, 7, 7.4, 7.3, 8-bullseye, 8.1-bullseye, 8.0-bullseye, 7-bullseye, 7.4-bullseye, 7.3-bullseye, 8-buster, 8.1-buster, 8.0-buster, 7-buster, 7.4-buster
ARG VARIANT=8.1-bullseye

FROM mcr.microsoft.com/vscode/devcontainers/php:0-${VARIANT} as base


EXPOSE 80
ENV APP_ENV=prod
ENV APACHE_LOCK_DIR    /var/lock/apache2
ENV APACHE_LOG_DIR     /var/log/apache2
ENV APACHE_PID_FILE    /var/run/apache2/apache2.pid
ENV APACHE_SERVER_NAME php-docker-base-linkorb

COPY --from=composer /usr/bin/composer /usr/bin/composer

# Install MariaDB client
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y mariadb-client \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install php-mysql driver
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Install ansible
RUN apt-get update && \
  apt-get install -y gcc python-dev libkrb5-dev && \
  apt-get install python3-pip -y && \
  pip3 install --upgrade pip && \
  pip3 install --upgrade virtualenv && \
  pip3 install ansible

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi
RUN echo "xdebug.mode=off" | tee '/usr/local/etc/php/conf.d/xdebug.ini'


RUN mkdir -p /app/config/secrets/dev \
  && mkdir -p /app/public/build \
  && a2enmod rewrite \
  && a2enmod headers


# install reviewdog
RUN mkdir -p /opt

WORKDIR /opt/
RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s
RUN mv /opt/bin/reviewdog /usr/local/bin


WORKDIR /workspace

COPY --from=jakzal/phpqa /tools /tools
ENV PATH="/tools:$PATH"

USER root
