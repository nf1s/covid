import requests
from pydantic import BaseModel, Field

URL = "https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query?f=json&where=Confirmed%20%3E%200&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&resultOffset=0&resultRecordCount=200&cacheHint=true"


class Covid(BaseModel):
    country: str = Field(..., alias="Country_Region")
    confirmed: int = Field(..., alias="Confirmed")
    deaths: int = Field(..., alias="Deaths")
    recovered: int = Field(..., alias="Recovered")
    latitude: float = Field(..., alias="Lat")
    longitude: float = Field(..., alias="Long_")
    last_update: int = Field(..., alias="Last_Update")


def cases():
    response = requests.get(URL)
    return response.json()["features"]


def data():
    return [Covid(**case["attributes"]).dict() for case in cases()]
