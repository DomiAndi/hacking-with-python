#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from os import path
from progress.bar import Bar

def obtener_plugins(url):
    # Verifica si el archivo 'wp_plugins.txt' existe
    if path.exists('wp_plugins.txt'):
        # Abre el archivo y lee las líneas
        with open('wp_plugins.txt', 'r') as archivo:
            plugins = archivo.read().splitlines()  # lee las líneas y las separa en una lista
            
        plugins_encontrados = []  # Lista para almacenar los plugins encontrados
        barra_progreso = Bar('Progreso:', max=len(plugins))  # Barra de progreso
        
        for plugin in plugins:
            barra_progreso.next()  # Actualiza la barra de progreso
            try:
                # Realiza una solicitud GET para verificar si el plugin existe
                respuesta = requests.get(url + '/' + plugin)
                if respuesta.status_code == 200:
                    # Si el plugin está disponible, lo agrega a la lista
                    plugins_encontrados.append(plugin)
            except requests.exceptions.RequestException as e:
                # Si ocurre un error de conexión, se captura y se ignora el plugin
                print(f"Error al acceder a {plugin}: {e}")
                pass
        
        barra_progreso.finish()  # Finaliza la barra de progreso
        
        # Imprime los plugins encontrados
        if plugins_encontrados:
            for plugin in plugins_encontrados:
                print(f"Plugin encontrado: {plugin}")
        else:
            print("No se encontraron plugins.")
    else:
        print("El archivo 'wp_plugins.txt' no existe.")

def main():
    url = ""  # URL base del sitio web (reemplazar con la URL real)
    obtener_plugins(url)

if __name__ == '__main__':
    try:
        main()  # Llama a la función principal
    except KeyboardInterrupt:
        print("Proceso interrumpido.")
        exit()
