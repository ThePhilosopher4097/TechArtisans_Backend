# importing packages
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd


# get link and return a beautified(structured) html content
def get_url(url):
    req = requests.get(url)
    if req.status_code != 200:
        print(f'failed to extract {url}')
    soup = BeautifulSoup(req.content, 'html.parser')
    
    return soup 


