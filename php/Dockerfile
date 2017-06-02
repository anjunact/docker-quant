from php:7.1.5-apache
ADD debian8.sources /etc/apt/sources.list
run apt-get update && apt-get install  -y apt-utils libpq-dev
run docker-php-ext-install pdo_mysql  pdo_pgsql