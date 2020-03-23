# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on worldometers.info statistics

"""
import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
