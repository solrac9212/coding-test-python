# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests
from colorama import Fore, init
init()
def run():
    
    r = requests.get('https://api.chucknorris.io/jokes/random')
    with open('joker.txt', 'w') as dataFile:
        data=r.json()
        json.dump(data['value'], dataFile, indent=4)   
        print(Fore.BLUE + json.dumps(r.json()))   
        return 1

 