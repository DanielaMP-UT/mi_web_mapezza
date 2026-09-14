FROM php:8.2-apache

# Copiar todo el contenido del sitio web al contenedor
COPY ./mi_app /var/www/html/

# Ajustar permisos para Apache
RUN chown -R www-data:www-data /var/www/html

EXPOSE 80