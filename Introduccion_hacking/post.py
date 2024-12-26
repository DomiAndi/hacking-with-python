#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse
import json
from os import path

# Configuración de argparse para manejar la entrada de archivos
parser = argparse.ArgumentParser(description='Envía una petición POST a una URL.')
parser.add_argument('-f', '--file', required=True, help='Archivo con los datos a enviar')
parser.add_argument('-u', '--url', required=True, help='URL de destino para enviar la solicitud POST')
parser = parser.parse_args()

def leer_datos_archivo(archivo):
    """Lee los datos del archivo y los convierte a un diccionario (suponiendo que es JSON o formato similar)."""
    if not path.exists(archivo):
        print(f"El archivo {archivo} no existe.")
        return None
    
    with open(archivo, 'r') as f:
        try:
            # Intentamos leer el archivo como JSON
            return json.load(f)
        except json.JSONDecodeError:
            print("Error: El archivo no tiene un formato JSON válido.")
            return None

def enviar_post(url, datos):
    """Envía una solicitud POST con los datos especificados a la URL."""
    try:
        # Enviar la solicitud POST con los datos
        response = requests.post(url, json=datos)
        
        # Verificar la respuesta
        if response.status_code == 200:
            print("Datos enviados exitosamente.")
            print("Respuesta del servidor:", response.json())
        else:
            print(f"Error al enviar los datos. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud POST: {e}")

def main():
    # Leer los datos desde el archivo proporcionado
    datos = leer_datos_archivo(parser.file)
    
    if datos:
        # Si los datos fueron leídos correctamente, enviamos la solicitud POST
        enviar_post(parser.url, datos)
    else:
        print("No se pudieron leer los datos del archivo.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo del script.")
