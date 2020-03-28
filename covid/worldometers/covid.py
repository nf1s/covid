# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on worldometers.info statistics

"""
import requests
from bs4 import BeautifulSoup
from covid.worldometers.models import CovidModel
from covid import config

URL = "https://www.worldometers.info/coronavirus/"

SOURCE = config.WORLDOMETERS


class Covid:
    def __init__(self):
        self._url = URL
        self._data = {}
        self._fetch()
        self._set_data()
        self.source = SOURCE

    def _fetch(self):
        """Method get all data when the class is inistantiated
            1. parses html
            2. gets all country data
        """
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
        """Method formats data to make it easily callable by country name
        """

        countries = (
            [attr.text.strip() for attr in row if attr != "\n"]
            for row in self._rows
        )
        self._data = {country[0].lower(): country for country in countries}

    def _format(self, _list: list) -> list:
        """Method formats a list and returns a fomatted one
        1. removes ','
        2. if there is no value it adds 0
        
        Args:
            _list (list): input list to be formatted
        
        Returns:
            list: output formatted list
        """
        _list = [val.strip().replace(",", "") for val in _list]
        return [val if val else 0 for val in _list]

    def get_data(self) -> list:
        """Method returns a list of all of the data from worldometers after being formatted
        
        Returns:
            list: List of country data
        """

        return [
            CovidModel(**dict(zip(self._headers, self._format(val)))).dict()
            for val in self._data.values()
        ]

    def get_status_by_country_name(self, country_name: str) -> dict:
        """Method gets country status
        
        Args:
            country_name (str): country name e.g "Sweden"
        
        Raises:
            ValueError: when country name is not correct
        
        Returns:
            dict: Country information
        """
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

    def list_countries(self) -> list:
        return list(self._data.keys())

    @staticmethod
    def _to_num(string: str) -> int:
        """formats string numbers and converts them to an integer
        e.g '123,456' -> 123456
        
        Args:
            string (str): input string number
        
        Returns:
            int: output integer number
        """
        return int(string.strip().replace(",", ""))

    def get_total_confirmed_cases(self) -> int:
        """Method gets the total number of confirmed cases
        
        Returns:
            int: Number of confirmed cases
        """
        return self._to_num(self._total_cases[0].span.text)

    def get_total_deaths(self) -> int:
        """Method gets the total number of deaths
        
        Returns:
            int: Total number of deaths
        """
        return self._to_num(self._total_cases[1].span.text)

    def get_total_recovered(self) -> int:
        """Method gets the total number of recovered cases
        
        Returns:
            int: Total number of recovered cases
        """
        return self._to_num(self._total_cases[2].span.text)

    def get_total_active_cases(self) -> int:
        """Method gets the total number of active cases
        
        Returns:
            int: Total number of active cases
        """
        confirmed = self.get_total_confirmed_cases()
        deaths = self.get_total_deaths()
        recovered = self.get_total_recovered()
        return confirmed - (recovered + deaths)
