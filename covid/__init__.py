# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on John Hopkins University statisticks

"""
from urllib.parse import ParseResult, urlparse, urlencode

import requests
from pydantic import BaseModel, Field


class CovidModel(BaseModel):
    """Dataclass acts as a Model for Covid data

    """

    id: str = Field(..., alias="OBJECTID")
    country: str = Field(..., alias="Country_Region")
    confirmed: int = Field(..., alias="Confirmed")
    active: int = Field(..., alias="Active")
    deaths: int = Field(..., alias="Deaths")
    recovered: int = Field(..., alias="Recovered")
    latitude: float = Field(..., alias="Lat")
    longitude: float = Field(..., alias="Long_")
    last_update: int = Field(..., alias="Last_Update")


class CountryModel(BaseModel):
    """Dataclass acts as a Model for Countries data

    """

    id: str = Field(..., alias="OBJECTID")
    name: str = Field(..., alias="Country_Region")


class Covid:
    """Class handells all functionality

    """

    @staticmethod
    def __all_url() -> str:
        """Method returns the url used to fetch all data from John hopkins server
        
        Returns:
            str: URL for getting all Covid data
        """
        url = urlparse("https://services1.arcgis.com")
        path = "/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
        query = {}
        query["f"] = "json"
        query["where"] = "Confirmed > 0"
        query["returnGeometry"] = "false"
        query["spatialRel"] = "esriSpatialRelIntersects"
        query["outFields"] = "*"
        query["orderByFields"] = "Confirmed desc"
        query["resultOffset"] = "0"
        query["resultRecordCount"] = "200"
        query["cacheHint"] = "true"
        url = ParseResult(
            scheme=url.scheme,
            netloc=url.hostname,
            path=path,
            query=urlencode(query),
            params=url.params,
            fragment=url.fragment,
        )
        return url.geturl()

    @staticmethod
    def __country_url(object_id: str) -> str:
        """Method formats and encodes the URL for a specific country information regarding Covid
        
        Args:
            country (str): Country name e.g. "sweden"
        
        Returns:
            str: Formatted encoded URL for the requested country
        """
        url = urlparse("https://services1.arcgis.com")
        path = "/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
        query = {}
        query["f"] = "json"
        query["where"] = f"OBJECTID = {object_id}"
        query["returnGeometry"] = "false"
        query["spatialRel"] = "esriSpatialRelIntersects"
        query["outFields"] = "*"
        query["resultOffset"] = "0"
        query["resultRecordCount"] = "1"
        query["cacheHint"] = "true"
        url = ParseResult(
            scheme=url.scheme,
            netloc=url.hostname,
            path=path,
            query=urlencode(query),
            params=url.params,
            fragment=url.fragment,
        )
        return url.geturl()

    @staticmethod
    def __total_url_by_case(case: str) -> str:
        """Method formats and encodes the URL for a specific case (Deaths, Confirmed cases and Recovered cases)
        
        Args:
            case (str): cases = "Deaths", "Confirmed" and "Recovered"
        
        Returns:
            str: Formatted encoded URL for the requested case
        """
        url = urlparse("https://services1.arcgis.com")
        path = "/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
        query = {}
        query["f"] = "json"
        query["where"] = "Confirmed > 0"
        query["returnGeometry"] = "false"
        query["spatialRel"] = "esriSpatialRelIntersects"
        query["outFields"] = "*"
        query["outStatistics"] = (
            '[{"statisticType":"sum","onStatisticField":"'
            + case
            + '","outStatisticFieldName":"value"}]'
        )

        query["cacheHint"] = "true"

        url = ParseResult(
            scheme=url.scheme,
            netloc=url.hostname,
            path=path,
            query=urlencode(query),
            params=url.params,
            fragment=url.fragment,
        )
        return url.geturl()

    def __get_total_by_case(self, case: str) -> int:
        """Method fetchs the total value of a specific case (Deaths, Confirmed cases and Recovered cases)
        
        Args:
            case (str): cases = "Deaths", "Confirmed" and "Recovered"
        
        Returns:
            str: Total value
        """
        url = self.__total_url_by_case(case)
        response = requests.get(url).json()
        try:
            return response["features"][0]["attributes"]["value"]
        except KeyError:
            raise Exception(response)

    def get_all_cases(self) -> list:
        """Method fetches all data related to Covid
        
        Returns:
            list: list of Covid data
                example:
                        [
                            {
                                'id': '53',
                                'country': 'China',
                                'confirmed': 81020,
                                'active': 9960,
                                'deaths': 3217,
                                'recovered': 67843,
                                'latitude': 30.5928,
                                'longitude': 114.3055,
                                'last_update': 1584097775000
                            }
        """

        response = requests.get(self.__all_url()).json()
        try:
            return response["features"]
        except KeyError:
            raise Exception(response)

    def get_data(self) -> list:
        """Method fetches all data related to Covid
        """

        cases = self.get_all_cases()
        return [CovidModel(**case["attributes"]).dict() for case in cases]

    def get_total_active_cases(self) -> int:
        """Method fetches and returns total number of active cases
        
        Returns:
            int: Total number of active at this time
        """
        return self.__get_total_by_case("Active")

    def get_total_deaths(self) -> int:
        """Method fetches and returns total deaths number
        
        Returns:
            int: Total number of deaths at this time
        """
        return self.__get_total_by_case("Deaths")

    def get_total_confirmed_cases(self) -> int:
        """Method fetches and returns the total number of confirmed cases
        
        Returns:
            int: Total number of confirmed cases at this time
        """
        return self.__get_total_by_case("Confirmed")

    def get_total_recovered(self) -> int:
        """Method fetches and returns the total number of recovered cases
        
        Returns:
            int: Total number of recovered cases at this time
        """
        return self.__get_total_by_case("Recovered")

    def list_countries(self) -> list:
        """Method returns the names of all countries available, so that it can be used when
        querying status by a specific country

        Returns:
            list[str]: list of country names
        """
        cases = self.get_all_cases()
        return [CountryModel(**case["attributes"]).dict() for case in cases]

    def get_status_by_country_id(self, country_id) -> dict:
        """Method fetches and returns specific country information related to coronavirus
        
        Args:
            country (str):  Country name e.g. "sweden"
        
        Returns:
            dict: Country related information regarding Coronavirus
            example:
                    {
                        'country': 'Sweden',
                        'confirmed': 355,
                        'active': 334,
                        'deaths': 0,
                        'recovered': 1,
                        'latitude': 63.0,
                        'longitude': 16.0,
                        'last_update': 1583893094000
                    }
        """
        url = self.__country_url(country_id)
        response = requests.get(url).json()
        try:
            case = response["features"][0]["attributes"]
        except KeyError:
            return Exception(response)

        return CovidModel(**case).dict()

    def get_status_by_country_name(self, country_name) -> dict:
        """Method fetches and returns specific country information related to coronavirus
        
        Args:
            country (str):  Country name e.g. "sweden"
        
        Returns:
            dict: Country related information regarding Coronavirus
            example:
                    {
                        'country': 'Sweden',
                        'confirmed': 355,
                        'active': 334,
                        'deaths': 0,
                        'recovered': 1,
                        'latitude': 63.0,
                        'longitude': 16.0,
                        'last_update': 1583893094000
                    }
        """
        country = filter(
            lambda country: country["name"] == country_name.title(),
            self.list_countries(),
        )
        country = next(country)
        url = self.__country_url(country["id"])
        response = requests.get(url).json()

        try:
            case = response["features"][0]["attributes"]
        except KeyError:
            return Exception(response)

        return CovidModel(**case).dict()
