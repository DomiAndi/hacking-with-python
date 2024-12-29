#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def main():
    url = "" # URL de la página
    cabecera = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    peticion = requests.get(url, headers=cabecera)
    soup = BeautifulSoup(peticion.text, 'html5lib')
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            version = v.get('content')
    print(version)
    
if __name__ == '__main__':
    try:
        
        main()
    except KeyboardInterrupt:
        print("Saliendo del programa...")
        exit()