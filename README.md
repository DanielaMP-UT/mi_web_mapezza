# Aplicación Web Responsiva - MAPEZZA
Este proyecto consiste en el desarrollo y despliegue de una aplicación web sencilla y responsiva para el menú de un restaurante denominado **MAPEZZA**.

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio.
   
### 2. Abre el proyecto en Visual Studio o en tu editor de código de tu preferencia.

### 3. Abre una terminal en la raíz del proyecto y ejecuta los siguientes comandos:

 #### Contruir la imagen.
    docker compose build

 #### Levantar el contenedor.
    docker compose up -d

  #### Comprobar estado del conteendor.
    docker compose ps

### 4. Ejecución de ambas versiones - Estática y Dinámica:
Esta aplicación cuenta con dos versiones: una **estática** (con los platillos codificados directamente en el HTML) y una **dinámica** (que consume los datos desde un archivo JSON mediante JavaScript).

   ### Acceso a las Versiones Web
   Asegúrate de tener Docker corriendo e iniciar el contenedor previamente construido.
   Una vez iniciado el contenedor, abre tu navegador e ingresa a las siguientes direcciones según la versión que desees visualizar:

   #### Versión Estática
   URL: ```http://localhost:8081```(o ```http://localhost:8081/index.html```)

   #### Versión Dinámica
   URL: ```http://localhost:8081/index_v1.html```


## Comportamiento de la Aplicación
La aplicación **MAPEZZA** está diseñada siguiendo el enfoque con **Bootstrap 5**, garantizando una navegación intuitiva.

### Funcionalidades y Secciones Principales:

1. **Barra de Navegación Responsiva:**
   * Incluye el logotipo/nombre del restaurante y enlaces a las secciones principales (*Inicio*, *Menú*, *Promociones*, *Contacto*).

2. **Sección Principal:**
   * Presentación visual atractiva con mensaje de bienvenida e imágenes adaptables que se reajustan proporcionalmente al ancho del dispositivo.

3. **Menú de Platillos:**
   * Organizado utilizando el **Grid System** de Bootstrap.
   * En pantallas grandes (Desktop) muestra los platillos ordenados en columnas paralelas.
   * En pantallas pequeñas (Mobile) reorganiza las tarjetas (*Cards*) en una sola columna para facilitar el desplazamiento vertical (*scroll*).

