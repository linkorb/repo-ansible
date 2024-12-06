FROM ubuntu:24.04

RUN apt-get update && apt-get install -y php-cli php-xml composer ansible-lint

ARG phpstan_version=2.0.1
RUN wget "https://github.com/phpstan/phpstan/releases/download/$phpstan_version/phpstan.phar" \
&& chmod +x phpstan.phar \
&& mv phpstan.phar /usr/local/bin/phpstan

ARG php_cs_fixer_version=v3.64.0
RUN wget "https://github.com/PHP-CS-Fixer/PHP-CS-Fixer/releases/download/$php_cs_fixer_version/php-cs-fixer.phar" \
&& chmod +x php-cs-fixer.phar \
&& mv php-cs-fixer.phar /usr/local/bin/php-cs-fixer

ARG twig_cs_fixer_version=3.3.1
RUN wget "https://github.com/VincentLanglet/Twig-CS-Fixer/releases/download/$twig_cs_fixer_version/twig-cs-fixer.phar" \
&& chmod +x twig-cs-fixer.phar \
&& mv twig-cs-fixer.phar /usr/local/bin/twig-cs-fixer

ARG reviewdog_version=0.20.2
RUN wget "https://github.com/reviewdog/reviewdog/releases/download/v$reviewdog_version/reviewdog_${reviewdog_version}_Linux_x86_64.tar.gz" \
&& tar xf "reviewdog_${reviewdog_version}_Linux_x86_64.tar.gz" \
&& mv reviewdog /usr/local/bin/reviewdog

WORKDIR /app
#CMD reviewdog -filter-mode=nofilter

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
