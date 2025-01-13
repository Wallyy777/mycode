#!/usr/bin/env python3
"Making a call to pokeapi.co with requests"
import requests


def main():
    # This is liking typing URL in browser
    response = requests.get("https://pokeapi.co/api/v2/pokemon/35/")

    decodedJson = response.json()

    print(decodedJson.get('name'))

if __name__ == '__main__':
    main()
    
