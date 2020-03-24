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

    def _fetch(self):
        response = requests.get(self._url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", attrs={"class": "main_table_countries"})
        headers = table.find_all("th")
        self._headers = self._format_headers(headers)
        self._rows = table.tbody.find_all("tr")
        self._total_cases = soup.find_all(
            "div", attrs={"class": "maincounter-number"}
        )

    def _format_headers(self, headers):
        headers = [underscore(header.text) for header in headers]
        headers[0] = headers[0].split(",").pop(0)
        headers[8] = headers[8].replace("\xa0", "")
        return headers

    def _set_data(self):

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

    def list_countries(self):
        return self._data.keys()

    @staticmethod
    def _to_num(string):
        return int(string.strip().replace(",", ""))

    def get_total_confirmed_cases(self):
        return self._to_num(self._total_cases[0].span.text)

    def get_total_deaths(self):
        return self._to_num(self._total_cases[1].span.text)

    def get_total_recovered(self):
        return self._to_num(self._total_cases[2].span.text)

    def get_total_active_cases(self):
        confirmed = self.get_total_confirmed_cases()
        deaths = self.get_total_deaths()
        recovered = self.get_total_recovered()
        return confirmed - (recovered + deaths)
