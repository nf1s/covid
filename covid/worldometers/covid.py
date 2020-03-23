# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on worldometers.info statistics

"""
import requests
from bs4 import BeautifulSoup
from inflection import underscore

URL = "https://www.worldometers.info/coronavirus/"


class Covid:
    def __init__(self):
        self._url = URL
        self._data = {}
        self.__fetch()
        self.__set_data()

    def __fetch(self):
        response = requests.get(self._url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", attrs={"class": "main_table_countries"})
        headers = table.find_all("th")
        self._headers = self.__format_headers(headers)
        self._rows = table.tbody.find_all("tr")

    def __format_headers(self, headers):
        headers = [underscore(header.text) for header in headers]
        headers[0] = headers[0].split(",").pop(0)
        headers[8] = headers[8].replace("\xa0", "")
        return headers

    def __set_data(self):

        countries = (
            [attr.text.strip() for attr in row if attr != "\n"]
            for row in self._rows
        )
        self._data = {country[0].lower(): country for country in countries}

    def get_data(self):
        return {
            key: dict(zip(self._headers, val))
            for (key, val) in self._data.items()
        }

    def get_status_by_country_name(self, name):
        return dict(zip(self._headers, self._data[name.lower()]))
