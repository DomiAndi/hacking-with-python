#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib

def main():
    url = urllib.urlopen("") # URL de la Web
    for u in json.loads(url.read()):
        user = u['slug']
    print(user)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo...')
        exit()