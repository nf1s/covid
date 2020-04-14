# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on worldometers.info statistics

"""
import requests
from bs4 import BeautifulSoup
from covid.worldometers.models import CovidModel
from covid import config
from pydantic import ValidationError

URL = "https://www.worldometers.info/coronavirus/"

SOURCE = config.WORLDOMETERS


class Covid:
    def __init__(self):
        self.__url = URL
        self.__data = {}
        self.__fetch()
        self.__set_data()
        self.source = SOURCE

    def __fetch(self):
        """Method get all data when the class is inistantiated
            1. parses html
            2. gets all country data
        """
        response = requests.get(self.__url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", attrs={"class": "main_table_countries"})
        headers = table.find_all("th")
        self.__headers = [
            header.text.replace("\xa0", "") for header in headers
        ]
        self.__rows = table.tbody.find_all("tr")
        self.__total_cases = soup.find_all(
            "div", attrs={"class": "maincounter-number"}
        )

    def __set_data(self):
        """Method formats data to make it easily callable by country name
        """

        countries = (
            [attr.text.strip() for attr in row if attr != "\n"]
            for row in self.__rows
        )
        self.__data = {country[0].lower(): country for country in countries}

    def __format(self, _list: list) -> list:
        """Method formats a list and returns a fomatted one
        1. removes ','
        2. if there is no value it adds 0
        
        Args:
            _list (list): input list to be formatted
        
        Returns:
            list: output formatted list
        """
        _list = [val.strip().replace(",", "") for val in _list]
        return [val if val and val != "N/A" else 0 for val in _list]

    def get_data(self) -> list:
        """Method returns a list of all of the data from worldometers after being formatted
        
        Returns:
            list: List of country data
        """
        return [
            CovidModel(**dict(zip(self.__headers, self.__format(val)))).dict()
            for val in self.__data.values()
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
                    self.__headers,
                    self.__format(self.__data[country_name.lower()]),
                )
            )
        except KeyError:
            raise ValueError(
                f"There is no country called '{country_name}', to check available country names use `list_countries()`"
            )
        return CovidModel(**country_data).dict()

    def list_countries(self) -> list:
        return list(self.__data.keys())

    @staticmethod
    def __to_num(string: str) -> int:
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
        return self.__to_num(self.__total_cases[0].span.text)

    def get_total_deaths(self) -> int:
        """Method gets the total number of deaths
        
        Returns:
            int: Total number of deaths
        """
        return self.__to_num(self.__total_cases[1].span.text)

    def get_total_recovered(self) -> int:
        """Method gets the total number of recovered cases
        
        Returns:
            int: Total number of recovered cases
        """
        return self.__to_num(self.__total_cases[2].span.text)

    def get_total_active_cases(self) -> int:
        """Method gets the total number of active cases
        
        Returns:
            int: Total number of active cases
        """
        confirmed = self.get_total_confirmed_cases()
        deaths = self.get_total_deaths()
        recovered = self.get_total_recovered()
        return confirmed - (recovered + deaths)
