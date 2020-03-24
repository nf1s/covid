# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on worldometers.info statistics

"""
import requests
from bs4 import BeautifulSoup
from inflection import underscore
from .models import CovidModel

URL = "https://www.worldometers.info/coronavirus/"


class Covid:
    def __init__(self):
        self._url = URL
        self._data = {}
        self._fetch()
        self._set_data()

    def _fetch(self):
        response = requests.get(self._url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", attrs={"class": "main_table_countries"})
        headers = table.find_all("th")
        self._headers = [header.text.replace("\xa0", "") for header in headers]
        self._rows = table.tbody.find_all("tr")
        self._total_cases = soup.find_all(
            "div", attrs={"class": "maincounter-number"}
        )

    def _set_data(self):
        countries = (
            [attr.text.strip() for attr in row if attr != "\n"]
            for row in self._rows
        )
        self._data = {country[0].lower(): country for country in countries}

    def _format(self, _list):
        _list = [val.strip().replace(",", "") for val in _list]
        return [val if val else 0 for val in _list]

    def get_data(self):

        return [
            CovidModel(**dict(zip(self._headers, self._format(val)))).dict()
            for val in self._data.values()
        ]

    def get_status_by_country_name(self, country_name):
        try:
            country_data = dict(
                zip(
                    self._headers,
                    self._format(self._data[country_name.lower()]),
                )
            )
        except KeyError:
            raise ValueError(
                f"There is no country called '{country_name}', to check available country names use `list_countries()`"
            )
        return CovidModel(**country_data).dict()

    def list_countries(self):
        return list(self._data.keys())

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
