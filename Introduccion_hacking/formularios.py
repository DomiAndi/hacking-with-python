#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def obtener_busqueda():
    """Obtiene la consulta de búsqueda desde la línea de comandos o solicita al usuario."""
    parser = argparse.ArgumentParser(description="Terminal Browser")
    parser.add_argument('-b', '--search', help="Search option", required=True)  # Argumento obligatorio
    args = parser.parse_args()

    # Si el parámetro de búsqueda no está presente, se solicita al usuario
    if not args.search:
        args.search = input("Por favor, ingresa el término de búsqueda: ")
    
    return args.search

def buscar_en_google(search_query):
    """Busca el término proporcionado en Google y devuelve los enlaces HTTPS encontrados."""
    url = "https://www.google.com/search?q=" + search_query
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    # Realizamos la solicitud HTTP usando requests
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error al hacer la solicitud: {response.status_code}")
        return []

    return obtener_links_https(response.text)

def obtener_links_https(html):
    """Extrae y devuelve los enlaces HTTPS de la página HTML utilizando BeautifulSoup."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []

    for link in soup.find_all('a', href=True):
        href = link.get('href')
        # Se asegura de que sea un enlace HTTPS válido
        if href.startswith("https://"):
            links.append(href)
    
    return links

def main():
    search_query = obtener_busqueda()  # Obtener la búsqueda desde la línea de comandos o entrada del usuario
    print(f"Buscando: {search_query}")
    
    # Buscar en Google
    https_links = buscar_en_google(search_query)

    if not https_links:
        print("No se encontraron enlaces HTTPS.")
    else:
        print(f"Enlaces HTTPS encontrados para '{search_query}':")
        for link in https_links:
            print(link)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo...")
        exit()
