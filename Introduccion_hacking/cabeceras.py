#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Detecta las cabeceras HTTP de una URL.')
    parser.add_argument('-t', '--target', required=True, help='URL objetivo para obtener las cabeceras')
    return parser.parse_args()

def fetch_headers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanzar un error para código 4xx/5xx
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el objetivo: {e}")
        return None

def print_headers(headers):
    if headers:
        for header, value in headers.items():
            print(f"{header}: {value}")
    else:
        print("No se pudo obtener las cabeceras.")

def main():
    args = parse_arguments()
    headers = fetch_headers(args.target)
    print_headers(headers)

if __name__ == '__main__':
    main()    