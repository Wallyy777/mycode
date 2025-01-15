#!usr/bin/python3

import pprint
import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API
    gotresp = requests.get(AOIF_BOOKS)
    
    ## Decode the response
    got_dj = gotsep.json()

    ## Print respomnse so we may read it
    pprint.pprint(got_dj)

    if __name__ == "__main__":
        main()


