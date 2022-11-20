# importing packages
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

def get_link(url):
    re = requests.get(url)
    soup = bf(re.content, 'html.parser')
    return soup