from fastapi import FastAPI, Response, status
import json
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson import json_util

app = FastAPI()

# Permite que el frontend (HTML/JS) consuma la API sin bloqueos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------ FUNCIÓN DE PRUEBA -------------------------------------------------------
@app.get("/")
def leer_raiz():
    """ Función de prueba
    Mensaje de bienvenida para los usuarios
    """
    return {"mensaje": "¡Hola desde FastAPI"}

#------------------------------------ FUNCIÓN GET QUE LEE EL ARCHIVO JSON ------------------------------------------
#lo regrese como respuesta
@app.get("/getdata")
def leer_datos(response: Response):

    # Define la ruta del archivo
    ruta_archivo = Path('menu.json')

    # Comprueba si el archivo existe
    if ruta_archivo.is_file():
        # Abre y lee el archivo JSON
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            #print("Contenido del archivo:")
            #print(datos)
            return {
                "Mensaje":"Datos obtenidos con exito",
                "Datos":datos
            }

# ------------------------------------ ERROR 404 ------------------------------------------
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
    
        return {
            "Mensaje": "No se pudieron extraer los precios, intente más tarde",
            "Datos":{}       
        }

# ------------------------------------ CONEXIÓN CON MONGODB COMPASS ------------------------------------------
@app.get("/getdatamdb")
def leer_datos_mdb(response: Response):

    client = MongoClient("mongodb://usuario_lectura:Danilee@localhost:27017/?authSource=menu_pwa")
    db = client["menu_pwa"]
    collection = db["platillos"]


    print("--- All Documents ---")
    all_documents = collection.find()

    lista_platillos = []

    #convertir cada documento a un json
    for doc in all_documents:

        # Convertimos el documento de MongoDB a una cadena JSON limpia
        doc_json_str = json_util.dumps(doc)

        #Lo cargamos como un diccionario JSON limpio
        doc_json = json.loads(doc_json_str)


        if "_id" in doc_json and isinstance(doc_json["_id"], dict) and "$oid" in doc_json["_id"]:
            doc_json["_id"] = doc_json["_id"]["$oid"]

        print(doc_json) #Imprime cada documento ya convertido a JSON
        lista_platillos.append(doc_json)

       
    if lista_platillos:
        return {
            "Mensaje": "Datos obtenidos con éxito desde MongoDB",
            "Datos": lista_platillos
        }
    else:
        # Si no hay datos en la colección, devolvemos 404
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "Mensaje": "No se pudieron extraer los precios, intente más tarde",
            "Datos": {}
        }


    # ruta_archivo = Path('menu.json')

    # # Comprueba si el archivo existe
    # if ruta_archivo.is_file():
    #     # Abre y lee el archivo JSON
    #     with open(ruta_archivo, 'r', encoding='utf-8') as f:
    #         datos = json.load(f)
    #         #print("Contenido del archivo:")
    #         #print(datos)
    #         return {
    #             "Mensaje":"Datos obtenidos con exito",
    #             "Datos":datos
    #         }
    # else:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    
    #     return {
    #         "Mensaje": "No se pudieron extraer los precios, intente más tarde",
    #         "Datos":{}       
    #     }
