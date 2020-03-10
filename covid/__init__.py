import requests
from pydantic import BaseModel, Field


class CovidModel(BaseModel):
    country: str = Field(..., alias="Country_Region")
    confirmed: int = Field(..., alias="Confirmed")
    deaths: int = Field(..., alias="Deaths")
    recovered: int = Field(..., alias="Recovered")
    latitude: float = Field(..., alias="Lat")
    longitude: float = Field(..., alias="Long_")
    last_update: int = Field(..., alias="Last_Update")


class Covid:
    def __init__(self):
        self._url = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query?f=json&where=Confirmed%20%3E%200&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&resultOffset=0&resultRecordCount=200&cacheHint=true"

    @property
    def _cases(self):
        response = requests.get(self._url)
        cases = response.json()["features"]
        return cases

    @property
    def data(self):
        return [
            CovidModel(**case["attributes"]).dict() for case in self._cases
        ]
