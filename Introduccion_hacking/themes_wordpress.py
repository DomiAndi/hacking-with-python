#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def main():
    agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    peticion = requests.get(url="", headers=agent) # URL de la página
    soup = BeautifulSoup(peticion.text, 'html5lib')
    for enlace in soup.find_all('link'):
        if '/wp-contet/themes/' in enlace.get('href'):
            the = enlace.get('href').split('/')
            if 'themes' in the:
                pos = the.index('themes')
                theme = the[pos+1]
                print(theme)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()