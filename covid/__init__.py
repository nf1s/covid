# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on John Hopkins University statisticks

"""
from urllib.parse import urlparse

import requests
from pydantic import BaseModel, Field

COUNTRY_MAP = {
    "china": "44",
    "italy": "97",
    "iran": "34",
    "republic of korea": "93",
    "south Korea": "93",
    "spain": "18",
    "france": "38",
    "germany": "16",
    "us": "57",
    "others": "14",
    "switzerland": "88",
    "japan": "61",
    "norway": "41",
    "netherlands": "19",
    "uk": "60",
    "sweden": "50",
    "denmark": "83",
    "belgium": "79",
    "austria": "59",
    "bahrain": "9",
    "singapore": "42",
    "malaysia": "58",
    "australia": "76",
    "canada": "1",
    "greece": "118",
    "iceland": "106",
    "israel": "105",
    "united arab emirates": "28",
    "kuwait": "64",
    "iraq": "81",
    "czech republic": "74",
    "india": "29",
    "san marino": "36",
    "thailand": "80",
    "egypt": "116",
    "finland": "48",
    "lebanon": "91",
    "philippines": "110",
    "portugal": "54",
    "viet nam": "35",
    "brazil": "2",
    "slovenia": "12",
    "indonesia": "49",
    "ireland": "71",
    "occupied palestinian territory": "103",
    "palestine": "103",
    "romania": "53",
    "poland": "84",
    "qatar": "96",
    "georgia": "82",
    "saudi arabia": "10",
    "russian federation": "15",
    "russia": "15",
    "algeria": "77",
    "argentina": "5",
    "pakistan": "20",
    "oman": "21",
    "ecuador": "73",
    "chile": "78",
    "croatia": "87",
    "south africa": "55",
    "costa rica": "67",
    "estonia": "90",
    "hungary": "113",
    "serbia": "117",
    "azerbaijan": "30",
    "peru": "40",
    "albania": "27",
    "belarus": "51",
    "panama": "65",
    "maldives": "102",
    "latvia": "112",
    "north macedonia": "22",
    "afghanistan": "32",
    "slovakia": "39",
    "luxembourg": "68",
    "mexico": "115",
    "bulgaria": "52",
    "brunei": "75",
    "tunisia": "92",
    "bosnia and herzegovina": "13",
    "french guiana": "23",
    "new zealand": "25",
    "dominican republic": "46",
    "malta": "100",
    "paraguay": "111",
    "senegal": "107",
    "lithuania": "3",
    "cambodia": "4",
    "bangladesh": "33",
    "republic of moldova": "66",
    "moldova": "85",
    "morocco": "86",
    "colombia": "94",
    "cyprus": "95",
    "martinique": "109",
    "bolivia": "6",
    "cameroon": "7",
    "burkina faso": "8",
    "channel islands": "11",
    "saint martin": "62",
    "faroe islands": "63",
    "nigeria": "72",
    "honduras": "114",
    "sri lanka": "119",
    "saint barthelemy": "17",
    "monaco": "24",
    "jamaica": "26",
    "turkey": "31",
    "mongolia": "37",
    "togo": "43",
    "armenia": "45",
    "ukraine": "47",
    "liechtenstein": "56",
    "andorra": "69",
    "gibraltar": "70",
    "bhutan": "98",
    "nepal": "99",
    "democratic republic of the congo": "101",
    "congo": "101",
    "holy see": "104",
    "jordan": "108",
}


class CovidModel(BaseModel):
    """Dataclass acts as a Model for Covid data

    """

    country: str = Field(..., alias="Country_Region")
    confirmed: int = Field(..., alias="Confirmed")
    deaths: int = Field(..., alias="Deaths")
    recovered: int = Field(..., alias="Recovered")
    latitude: float = Field(..., alias="Lat")
    longitude: float = Field(..., alias="Long_")
    last_update: int = Field(..., alias="Last_Update")


class Covid:
    """Class handells all functionality

    """

    @staticmethod
    def __all_url() -> str:
        """Method returns the url used to fetch all data from John hopkins server
        
        Returns:
            str: URL for getting all Covid data
        """
        url = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
        url += "?f=json&where=Confirmed > 0&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*"
        url += "&orderByFields=Confirmed desc&resultOffset=0&resultRecordCount=200&cacheHint=true"
        url = urlparse(url)
        return url.geturl()

    @staticmethod
    def __country_url(country: str) -> str:
        """Method formats and encodes the URL for a specific country information regarding Covid
        
        Args:
            country (str): Country name e.g. "sweden"
        
        Returns:
            str: Formatted encoded URL for the requested country
        """
        object_id = COUNTRY_MAP[country]
        url = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
        url += f"?f=json&where=OBJECTID = {object_id}&returnGeometry=false&spatialRel=esriSpatialRelIntersects"
        url += "&outFields=*&resultOffset=0&resultRecordCount=1&cacheHint=true"
        url = urlparse(url)
        return url.geturl()

    @staticmethod
    def __total_url_by_case(case: str) -> str:
        """Method formats and encodes the URL for a specific case (Deaths, Confirmed cases and Recovered cases)
        
        Args:
            case (str): cases = "Deaths", "Confirmed" and "Recovered"
        
        Returns:
            str: Formatted encoded URL for the requested case
        """
        url = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
        url += "?f=json&where=Confirmed > 0&returnGeometry=false&spatialRel=esriSpatialRelIntersects"
        url += (
            '&outFields=*&outStatistics=[{"statisticType":"sum","onStatisticField":"'
            + case
            + '","outStatisticFieldName":"value"}]&cacheHint=true'
        )
        url = urlparse(url)
        return url.geturl()

    def __get_total_by_case(self, case: str) -> int:
        """Method fetchs the total value of a specific case (Deaths, Confirmed cases and Recovered cases)
        
        Args:
            case (str): cases = "Deaths", "Confirmed" and "Recovered"
        
        Returns:
            str: Total value
        """
        url = self.__total_url_by_case(case)
        response = requests.get(url)
        return response.json()["features"][0]["attributes"]["value"]

    def get_data(self) -> list:
        """Method fetches all data related to Covid
        
        Returns:
            list: list of Covid data
                example:
                        [
                            {
                                'country': 'Mainland China',
                                'confirmed': 80756,
                                'deaths': 3136,
                                'recovered': 60096,
                                'latitude': 30.5928,
                                'longitude': 114.3055,
                                'last_update': 1582264984000
                            },
        """

        response = requests.get(self.__all_url())
        cases = response.json()["features"]
        return [CovidModel(**case["attributes"]).dict() for case in cases]

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
        return list(COUNTRY_MAP.keys())

    def get_status_by_country(self, country) -> dict:
        """Method fetches and returns specific country information related to coronavirus
        
        Args:
            country (str):  Country name e.g. "sweden"
        
        Returns:
            dict: Country related information regarding Coronavirus
            example:
                    {
                        'country': 'Sweden',
                        'confirmed': 355,
                        'deaths': 0,
                        'recovered': 1,
                        'latitude': 63.0,
                        'longitude': 16.0,
                        'last_update': 1583893094000
                    }
        """
        country = country.lower()
        url = self.__country_url(country)
        response = requests.get(url)
        case = response.json()["features"][0]["attributes"]
        return CovidModel(**case).dict()
