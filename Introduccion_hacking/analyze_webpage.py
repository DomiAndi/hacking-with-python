#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Wappalyzer import WebPage, Wappalyzer

def main():
    wappalyzer = Wappalyzer.latest()
    try:
        webpage = WebPage.new_from_url('http://example.com')
        technologies = wappalyzer.analyze(webpage)
        for technology in technologies:
            print("Tecnologia detectada: {}".format(technology))
    except:
        print('Error al analizar la pagina web')    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo...')
        exit()