# Aplicación Web Responsiva - MAPEZZA
Este proyecto consiste en el desarrollo y despliegue de una aplicación web sencilla y responsiva para el menú de un restaurante denominado **MAPEZZA**. La aplicación ahora cuenta la integración de  una base de datos MongoDB para la gestión dinámica de los platillos y una página personalizada para el manejo de errores 404.

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio.
   
### 2. Abre el proyecto en Visual Studio Code o en el editor de código de tu preferencia.

### 3. Abre una terminal en la raíz del proyecto y ejecuta los siguientes comandos:

 #### Construir la imagen.
    docker compose build

 #### Levantar el contenedor.
    docker compose up -d

  #### Comprobar estado del contenedor.
    docker compose ps



### 4. Ejecución de ambas versiones - Estática y Dinámica:
Esta aplicación cuenta con diferentes versiones desarrolladas evolutivamente: una **estática** (con platillos codificados en HTML) y versiones **dinámicas** que consumen datos desde un archivo JSON local o una base de datos **MongoDB** con manejo seguro de errores HTTP.

   ### Acceso a las Versiones Web
   Asegúrate de tener Docker corriendo e iniciar el contenedor previamente construido.
   Una vez iniciado el contenedor, abre tu navegador e ingresa a las siguientes direcciones según la versión que desees visualizar:

   #### Versión Estática (Versión Base)
   URL: ```http://localhost:8081```(o ```http://localhost:8081/index.html```)

   #### Versión Dinámica (Consumo básico de JSON)
   URL: ```http://localhost:8081/index_v1.html```

   #### Versión Dinámica v2 (Consumo JSON con petición segura y control de Error 404)
   URL: ```http://localhost:8081/index_v2.html```

   #### Versión Dinámica v3 (Consumo desde MongoDB con petición segura)
   URL: ```http://localhost:8081/index_v3.html```



## Comportamiento de la Aplicación
El backend está desarrollado en **FastAPI** y expone los siguientes endpoints para la consulta de información:

* `GET /getdata`: Lee la información del menú desde el archivo local `menu.json`. En caso de no encontrar el recurso o fallar la lectura, retorna un código de estado HTTP **404 Not Found**.

* `GET /getdatamdb`: Se conecta a la base de datos en **MongoDB** (`menu_pwa`), consulta la colección de platillos (`platillos`), convierte los documentos BSON/JSON e incluye control de respuestas de error.



### Cómo probar el manejo de errores HTTP 404
   La aplicación cuenta con mecanismos de resiliencia tanto en el backend (FastAPI) como en el frontend (`peticionSegura`). Para verificar el comportamiento ante una falla 404, se pueden seguir estos pasos:

   #### Opción 1. Probar Error 404 en la API basada en JSON (`/getdata`)
   1. Abre el archivo `mi_api/main.py`.
   2. En la función `leer_datos()`, cambia la ruta del archivo por un nombre inexistente:
      ```python
      # Cambiar:
      ruta_archivo = Path('menu.json')
      # Por:
      ruta_archivo = Path('otro_nombre.json')

   #### Opción 2. Probar Error 404 en la API basada en MongoDB
   1. Abre el archivo `mi_api/main.py`.
   2. En la función `leer_datos()`, cambia la colección objetivo por una colección vacía o inexistente:
      ```python
      # Cambiar:
      collection = db["platillos"]
      # Por:
      collection = db["otro_nombre"]

   
   
### Funcionalidades y Secciones Principales:

1. **Barra de Navegación Responsiva:**
   * Incluye el logotipo/nombre del restaurante y enlaces a las secciones principales (*Entradas*, *Plato Principal*, *Postres* y *Bebidas*).

2. **Sección Principal:**
   * Presentación visual atractiva con mensaje de bienvenida e imágenes adaptables que se reajustan proporcionalmente al ancho del dispositivo.

3. **Menú de Platillos:**
   * Organizado utilizando el **Grid System** de Bootstrap.
   * En pantallas grandes (Desktop) muestra los platillos ordenados en columnas paralelas.
   * En pantallas pequeñas (Mobile) reorganiza las tarjetas (*Cards*) en una sola columna para facilitar el desplazamiento vertical (*scroll*).

   4. **Manejo Seguro de Peticiones y Alertas de Error:**
   * Integración de una función auxiliar `peticionSegura` en el frontend que valida la respuesta y el tipo de contenido JSON.
   * En caso de interrupción del servicio o respuesta con código de error (404/500), la interfaz despliega dinámicamente un mensaje de alerta amigable para el usuario (*"No se pudieron extraer los precios, por favor intente más tarde"*).

